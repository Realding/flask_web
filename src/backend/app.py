from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_apispec import FlaskApiSpec

from .config import configs

db = SQLAlchemy()
docs = FlaskApiSpec()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='ApiSpecBlog',
            version='v1',
            openapi_version="3.0.2",
            plugins=[MarshmallowPlugin()],
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
    })

    CORS(app)
    db.init_app(app)
    docs.init_app(app)

    from backend.views.blog.article import ArticleResource
    app.add_url_rule('/articles', view_func=ArticleResource.as_view('article'))
    print(app.url_map)
    docs.register(ArticleResource, endpoint='article')
    
    with app.app_context():
        db.create_all()
    # from backend.views.blog import bp as blog_bp
    # app.register_blueprint(blog_bp)
    return app
