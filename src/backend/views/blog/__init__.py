from flask import Blueprint

bp = Blueprint('blog', __name__)

from .article import ArticleResource

bp.add_url_rule('/articles', view_func=ArticleResource.as_view('Article'))