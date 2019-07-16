from flask import Flask, Blueprint
from flask_restful import Api
from api.v1.posts import PostsResource, PostResource

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)

# Route
api_v1.add_resource(PostsResource, '/posts')
api_v1.add_resource(PostResource, '/posts/<int:post_id>')
