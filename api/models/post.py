from flask import abort
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from api.database import db, ma

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise BadRequest


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
