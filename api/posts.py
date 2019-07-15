from flask import abort
from flask_restful import Resource
from utils import find_item

posts = [
    {
        'id': 1,
        'content': 'A river',
        'author_id': 1,
    },
    {
        'id': 2,
        'content': 'A mountain',
        'author_id': 1,
    },
]

class PostResource(Resource):
    def get(self, post_id):
        post = find_item(posts, post_id)
        if post is None:
            abort(404)
        return post

class PostsResource(Resource):
    def get(self):
        return {
            'total': posts.__len__(),
            'data': posts,
        }
