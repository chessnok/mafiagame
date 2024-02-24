from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped
from werkzeug.security import check_password_hash, generate_password_hash

db: SQLAlchemy = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    username: Mapped[str] = db.Column(db.String(64), index=True, unique=True)
    email: Mapped[str] = db.Column(db.String(120), index=True, unique=True)
    password_hash: Mapped[str] = db.Column(db.String(128))
    telegram_id: Mapped[int] = db.Column(db.Integer)

    def to_json(self):
        return {"id": self.id, "username": self.username, "email": self.email}

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
