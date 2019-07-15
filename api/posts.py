from flask import Flask, abort, request
from flask_restful import Resource, Api
from api.utils import find_item

app = Flask(__name__)
app.url_map.strict_slashes = False # Make api address /posts works like /posts/
api = Api(app)

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

api.add_resource(PostsResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')


@app.errorhandler(404)
def not_found(e):
    return '', 404
