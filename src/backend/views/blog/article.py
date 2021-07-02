from flask_apispec import use_kwargs, marshal_with, MethodResource
from marshmallow import fields, Schema

from backend.models import db, Article


class ArticleSchema(Schema):
    class Meta:
        # 指定响应的数据字段
        fields = ['id', 'title', 'summary', 'content', 'create_time']


@marshal_with(ArticleSchema)
class ArticleResource(MethodResource):

    def get(self, article_id):
        if not article_id:
            return Article.query.all()
        return Article.query.filter_by(id=article_id).one()

    @use_kwargs(ArticleSchema)
    @marshal_with(ArticleSchema, code=201)
    def post(self, **kwargs):
        article = Article(**kwargs)
        db.session.add(article)
        db.session.commit()
        return article

    @use_kwargs(ArticleSchema)
    def put(self, article_id, **kwargs):
        article = Article.query.filter_by(id=article_id).one()
        article.__dict__.update(**kwargs)
        return article

    @marshal_with(None, code=204)
    def delete(self, article_id):
        article = Article.query.filter_by(id=article_id).one()
        db.session.delete(article)
        db.session.commit()
        return None
