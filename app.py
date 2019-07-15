from flask import Flask, Blueprint
from flask_restful import Api
from api.posts import PostsResource, PostResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(PostsResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')
