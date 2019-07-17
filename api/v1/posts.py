from flask import Flask, request, abort
from flask_restful import Resource
from api.models.post import Post, PostSchema
from api.database import db


def return_if_not_found(data):
    if data is None:
        abort(404)


class PostResource(Resource):
    def get(self, post_id):
        post_query = Post.query.get(post_id)
        if post_query is None:
            return_if_not_found(post_query)

        post_data = PostSchema().dump(post_query).data
        return post_data


class PostsResource(Resource):
    def get(self):
        posts_query = Post.query.all()
        return_if_not_found(posts_query)

        posts_data = PostSchema(many=True).dump(posts_query).data
        return {
            'total': posts_data.__len__(),
            'data': posts_data,
        }

    def post(self):
        if request.is_json:
            content = request.get_json().get('content')
        else:
            content = request.form.get("content")
        if content is None:
            abort(400)

        post = Post(content=content)
        db.session.add(post)
        db.session.commit()

        post_data = PostSchema().dump(post).data
        return post_data
