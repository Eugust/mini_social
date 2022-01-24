import graphene
from graphql_jwt.shortcuts import get_token
from graphql_jwt.decorators import login_required

from .types import PostType, CommentType, UserType
from posts.models import Post, Comment
from users.models import User


class CreateUserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    phone = graphene.String(required=True)
    gender = graphene.String(required=True)


class CreatePostInput(graphene.InputObjectType):
    text = graphene.String(required=True)


class PostInput(graphene.InputObjectType):
    id = graphene.ID()


class CreateCommentInput(graphene.InputObjectType):
    text = graphene.String(required=True)
    post = graphene.Field(PostInput)


class CommentInput(graphene.InputObjectType):
    id = graphene.ID()


class LikePostInput(graphene.InputObjectType):
    post = graphene.Field(PostInput)


class LikeCommentInput(graphene.InputObjectType):
    comment = graphene.Field(CommentInput)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()

    class Arguments:
        user_data = CreateUserInput(required=True)

    @staticmethod
    def mutate(root, info, user_data=None):
        user = User(
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            phone=user_data.phone,
            gender=user_data.gender
        )
        user.set_password(user_data.password)
        user.save()
        token = get_token(user)
        return CreateUser(user=user, token=token)


class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        post_data = CreatePostInput(required=True)

    @staticmethod
    @login_required
    def mutate(root, info, post_data=None):
        user = info.context.user
        post = Post.objects.create(
            text=post_data.text,
            author=user
        )
        return CreatePost(post=post)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        text = graphene.String()

    post = graphene.Field(PostType)

    @staticmethod
    @login_required
    def mutate(root, info, id, text):
        post = Post.objects.get(pk=id)
        if post:
            if info.context.user == post.author:
                post.text = text
                post.save()
                return UpdatePost(post=post)
            return None
        return None


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    post = graphene.Field(PostType)

    @staticmethod
    @login_required
    def mutate(root, info, id):
        post = Post.objects.get(pk=id)
        if info.context.user == post.author:
            post.delete()
        return None


class CreateComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        comment_data = CreateCommentInput(required=True)

    @staticmethod
    @login_required
    def mutate(root, info, comment_data=None):
        user = info.context.user
        post = Post.objects.get(id=comment_data.post.id)
        comment = Comment.objects.create(
            text=comment_data.text,
            author=user,
            post=post
        )
        return CreateComment(comment=comment)


class UpdateComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        text = graphene.String()

    comment = graphene.Field(CommentType)

    @staticmethod
    @login_required
    def mutate(root, info, id, text):
        comment = Comment.objects.get(pk=id)
        if comment:
            if info.context.user == comment.author:
                comment.text = text
                comment.save()
                return UpdateComment(comment=comment)
            return None
        return None


class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    comment = graphene.Field(CommentType)

    @staticmethod
    @login_required
    def mutate(root, info, id):
        comment = Comment.objects.get(pk=id)
        if info.context.user == comment.author:
            comment.delete()
        return None


class LikePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        data = LikePostInput(required=True)

    @staticmethod
    @login_required
    def mutate(root, info, data=None):
        user = info.context.user
        post = Post.objects.get(id=data.post.id)
        post.users_who_liked.add(user)
        return LikePost(post=post)


class LikeComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        data = LikeCommentInput(required=True)

    @staticmethod
    @login_required
    def mutate(root, info, data=None):
        user = info.context.user
        comment = Comment.objects.get(id=data.comment.id)
        comment.users_who_liked.add(user)
        return LikePost(comment=comment)
