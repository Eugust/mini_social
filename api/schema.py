import graphene

from .types import PostType, CommentType
from .mutations import (CreatePost, UpdatePost, CreateComment, UpdateComment, DeletePost, DeleteComment, CreateUser, LikePost, LikeComment)
from posts.models import Post, Comment


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    post = graphene.Field(PostType, post_id=graphene.Int())
    all_comments_of_post = graphene.List(CommentType, post_id=graphene.Int())
    comment_of_post = graphene.Field(
        CommentType,
        post_id=graphene.Int(),
        comment_id=graphene.Int()
    )

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_post(self, info, **kwargs):
        post_id = kwargs.get('post_id')
        return Post.objects.get(pk=post_id)

    def resolve_all_comments_of_post(self, info, **kwargs):
        post_id = kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id).all()

    def resolve_comment_of_post(self, info, **kwargs):
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

schema = graphene.Schema(query=Query, mutation=Mutation)
