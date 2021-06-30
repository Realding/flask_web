from datetime import datetime

from app import db


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


db.Model.to_dict = to_dict
db.Model.__table_args__ = {
    "mysql_charset": "utf8"
}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.Integer)
    summary = db.Column(db.Text)
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)  # last modify update time