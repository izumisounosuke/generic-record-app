from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """ユーザーモデル"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # リレーションシップ
    items = db.relationship('Item', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """パスワードをハッシュ化して設定"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """パスワードを検証"""
        return check_password_hash(self.password_hash, password)

class Item(db.Model):
    """記録項目モデル"""
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # リレーションシップ
    records = db.relationship('Record', backref='item', lazy=True, cascade='all, delete-orphan', order_by='Record.date.desc()')

class Record(db.Model):
    """記録データモデル"""
    __tablename__ = 'records'
    
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """JSON形式に変換"""
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'value': self.value
        }

