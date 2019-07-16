from flask import abort
from flask_restful import Resource
from api.models.post import Post
from utils import find_item

class PostResource(Resource):
    def get(self, post_id):
        post = find_item(posts, post_id)
        if post is None:
            abort(404)
        return post

class PostsResource(Resource):
    def get(self):
        posts = Post.query.all()
        return {
            'total': posts.__len__(),
            'data': posts,
        }
