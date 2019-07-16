from flask import abort
from flask_restful import Resource
from api.models.post import Post, post_schema, posts_schema

class PostResource(Resource):
    def get(self, post_id):
        post_query = Post.query.get(post_id)
        post = post_schema.dump(post_query).data
        if post is None:
            abort(404)
        return post

class PostsResource(Resource):
    def get(self):
        posts_query = Post.query.all()
        posts = posts_schema.dump(posts_query).data
        return {
            'total': posts.__len__(),
            'data': posts,
        }
