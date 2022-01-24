import graphene
import graphql_jwt

from .types import PostType, CommentType
from .mutations import (CreatePost, UpdatePost, CreateComment, UpdateComment, DeletePost, DeleteComment, CreateUser, LikePost, LikeComment)
from posts.models import Post, Comment


class Query(graphene.ObjectType):
    all_posts = graphene.List(
        PostType,
        first=graphene.Int(),
        skip=graphene.Int()
    )
    post = graphene.Field(PostType, post_id=graphene.Int())
    all_comments_post = graphene.List(
        CommentType,
        post_id=graphene.Int(),
        first=graphene.Int(),
        skip=graphene.Int()
    )
    comment_post = graphene.Field(
        CommentType,
        post_id=graphene.Int(),
        comment_id=graphene.Int()
    )

    def resolve_all_posts(self, info, first=None, skip=None, **kwargs):
        posts = Post.objects.all()
        if skip:
            posts = posts[skip:]
        if first:
            posts = posts[:first]
        return posts

    def resolve_post(self, info, **kwargs):
        post_id = kwargs.get('post_id')
        return Post.objects.get(pk=post_id)

    def resolve_all_comments_post(self, info, first=None, skip=None, **kwargs):
        post_id = kwargs.get('post_id')
        comments = Comment.objects.filter(post_id=post_id).all()
        if skip:
            comments = comments[skip:]
        if first:
            comments = comments[:first]
        return comments
        

    def resolve_comment_post(self, info, **kwargs):
        post_id = kwargs.get('post_id')
        comment_id = kwargs.get('comment_id')
        return Comment.objects.filter(post_id=post_id).get(pk=comment_id)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()
    like_post = LikePost.Field()
    like_comment = LikeComment.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
