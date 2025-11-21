from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from models import db, User, Item, Record
from datetime import datetime
from sqlalchemy import func
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///records.db').replace('postgres://', 'postgresql://')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# データベース初期化
with app.app_context():
    db.create_all()

def login_required(f):
    """ログイン必須デコレータ"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('ログインが必要です', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """ホーム画面（ダッシュボード）"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    items = Item.query.filter_by(user_id=user_id).order_by(Item.created_at.desc()).all()
    
    # 各項目の最新記録を取得
    items_with_latest = []
    for item in items:
        latest_record = Record.query.filter_by(item_id=item.id).order_by(Record.date.desc()).first()
        items_with_latest.append({
            'item': item,
            'latest_value': latest_record.value if latest_record else None,
            'latest_date': latest_record.date if latest_record else None,
            'record_count': Record.query.filter_by(item_id=item.id).count()
        })
    
    return render_template('index.html', items_with_latest=items_with_latest)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ログイン画面"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('ユーザー名とパスワードを入力してください', 'danger')
            return render_template('login.html')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('ログインに成功しました', 'success')
            return redirect(url_for('index'))
        else:
            flash('ユーザー名またはパスワードが正しくありません', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ユーザー登録画面"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        
        # バリデーション
        if not username or not password:
            flash('ユーザー名とパスワードを入力してください', 'danger')
            return render_template('register.html')
        
        if password != password_confirm:
            flash('パスワードが一致しません', 'danger')
            return render_template('register.html')
        
        if len(password) < 4:
            flash('パスワードは4文字以上で入力してください', 'danger')
            return render_template('register.html')
        
        # ユーザー名の重複チェック
        if User.query.filter_by(username=username).first():
            flash('このユーザー名は既に使用されています', 'danger')
            return render_template('register.html')
        
        # 新規ユーザー作成
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('アカウントが作成されました。ログインしてください', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    """ログアウト"""
    session.clear()
    flash('ログアウトしました', 'info')
    return redirect(url_for('login'))

@app.route('/item/new', methods=['POST'])
@login_required
def create_item():
    """新しい記録項目を作成"""
    name = request.form.get('name')
    unit = request.form.get('unit')
    
    if not name or not unit:
        flash('項目名と単位を入力してください', 'danger')
        return redirect(url_for('index'))
    
    user_id = session['user_id']
    
    # 項目名の重複チェック（同じユーザー内）
    existing_item = Item.query.filter_by(user_id=user_id, name=name).first()
    if existing_item:
        flash('この項目名は既に使用されています', 'danger')
        return redirect(url_for('index'))
    
    new_item = Item(user_id=user_id, name=name, unit=unit)
    db.session.add(new_item)
    db.session.commit()
    
    flash(f'項目「{name}」を作成しました', 'success')
    return redirect(url_for('index'))

@app.route('/item/<int:item_id>')
@login_required
def item_detail(item_id):
    """項目詳細ページ"""
    user_id = session['user_id']
    item = Item.query.filter_by(id=item_id, user_id=user_id).first_or_404()
    
    # 日付ごとに合計した記録を取得（履歴表示用）
    records_by_date = db.session.query(
        Record.date,
        func.sum(Record.value).label('total_value'),
        func.count(Record.id).label('count')
    ).filter_by(item_id=item_id).group_by(Record.date).order_by(Record.date.desc()).all()
    
    # テンプレート用に整形
    records = [{
        'date': r.date,
        'value': float(r.total_value),
        'count': r.count
    } for r in records_by_date]
    
    # 今日の日付を取得（デフォルト値として使用）
    today = datetime.now().date().isoformat()
    
    # 統計情報を計算（日付ごとの合計値で計算）
    stats = None
    if records:
        values = [r['value'] for r in records]
        stats = {
            'count': len(records),
            'max': max(values),
            'min': min(values),
            'avg': round(sum(values) / len(values), 2),
            'sum': sum(values)
        }
    
    return render_template('item_detail.html', item=item, records=records, today=today, stats=stats)

@app.route('/record/new', methods=['POST'])
@login_required
def create_record():
    """新しい記録を追加（同じ日付の記録があれば加算）"""
    item_id = request.form.get('item_id')
    date_str = request.form.get('date')
    value_str = request.form.get('value')
    
    if not item_id or not date_str or not value_str:
        flash('日付と値を入力してください', 'danger')
        return redirect(url_for('item_detail', item_id=item_id))
    
    user_id = session['user_id']
    item = Item.query.filter_by(id=item_id, user_id=user_id).first_or_404()
    
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        value = float(value_str)
        
        if value < 0:
            flash('値は0以上の数値を入力してください', 'danger')
            return redirect(url_for('item_detail', item_id=item_id))
        
        # 同じ日付の記録を検索
        existing_record = Record.query.filter_by(item_id=item_id, date=date).first()
        
        if existing_record:
            # 既存の記録に加算
            existing_record.value += value
            db.session.commit()
            flash(f'記録を追加しました（合計: {existing_record.value}{item.unit}）', 'success')
        else:
            # 新規記録を作成
            new_record = Record(item_id=item_id, date=date, value=value)
            db.session.add(new_record)
            db.session.commit()
            flash('記録を追加しました', 'success')
    except ValueError:
        flash('日付または値の形式が正しくありません', 'danger')
    
    return redirect(url_for('item_detail', item_id=item_id))

@app.route('/record/<int:record_id>/delete', methods=['POST'])
@login_required
def delete_record(record_id):
    """記録を削除"""
    record = Record.query.get_or_404(record_id)
    item = Item.query.get_or_404(record.item_id)
    
    # ユーザー認証
    if item.user_id != session['user_id']:
        flash('権限がありません', 'danger')
        return redirect(url_for('index'))
    
    item_id = record.item_id
    db.session.delete(record)
    db.session.commit()
    
    flash('記録を削除しました', 'success')
    return redirect(url_for('item_detail', item_id=item_id))

@app.route('/item/<int:item_id>/delete', methods=['POST'])
@login_required
def delete_item(item_id):
    """項目を削除"""
    item = Item.query.filter_by(id=item_id, user_id=session['user_id']).first_or_404()
    
    item_name = item.name
    db.session.delete(item)
    db.session.commit()
    
    flash(f'項目「{item_name}」を削除しました', 'success')
    return redirect(url_for('index'))

@app.route('/api/item/<int:item_id>/records')
@login_required
def get_item_records(item_id):
    """項目の記録データをJSON形式で返す（グラフ用）"""
    item = Item.query.filter_by(id=item_id, user_id=session['user_id']).first_or_404()
    
    # 同じ日付の記録を合計して返す
    records_by_date = db.session.query(
        Record.date,
        func.sum(Record.value).label('total_value')
    ).filter_by(item_id=item_id).group_by(Record.date).order_by(Record.date.asc()).all()
    
    data = {
        'labels': [record.date.isoformat() for record in records_by_date],
        'values': [float(record.total_value) for record in records_by_date]
    }
    
    return jsonify(data)

if __name__ == '__main__':
    # 開発環境用
    app.run(debug=True)

