from tkinter.tix import Tree
import graphene

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


class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)


class CreatePostInput(graphene.InputObjectType):
    text = graphene.String(required=True)
    author = graphene.Field(UserInput)


class PostInput(graphene.InputObjectType):
    id = graphene.ID()


class CreateCommentInput(graphene.InputObjectType):
    text = graphene.String(required=True)
    author = graphene.Field(UserInput)
    post = graphene.Field(PostInput)


class CommentInput(graphene.InputObjectType):
    id = graphene.ID()


class LikePostInput(graphene.InputObjectType):
    user = graphene.Field(UserInput)
    post = graphene.Field(PostInput)


class LikeCommentInput(graphene.InputObjectType):
    user = graphene.Field(UserInput)
    comment = graphene.Field(CommentInput)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        user_data = CreateUserInput(required=True)

    @classmethod
    def mutate(cls, root, info, user_data=None):
        user = User(
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            phone=user_data.phone,
            gender=user_data.gender
        )
        user.set_password(user_data.password)
        user.save()
        return CreateUser(user=user)


class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        post_data = CreatePostInput(required=True)

    @classmethod
    def mutate(cls, root, info, post_data=None):
        user = User.objects.get(username=post_data.author.username)
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

    @classmethod
    def mutate(cls, root, info, id, text):
        post = Post.objects.get(pk=id)
        if post:
            post.text = text
            post.save()
            return UpdatePost(post=post)
        return UpdatePost(post=None)


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, id):
        post = Post.objects.get(pk=id)
        post.delete()
        return None


class CreateComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        comment_data = CreateCommentInput(required=True)

    @classmethod
    def mutate(cls, root, info, comment_data=None):
        user = User.objects.get(username=comment_data.author.username)
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

    @classmethod
    def mutate(cls, root, info, id, text):
        comment = Comment.objects.get(pk=id)
        if comment:
            comment.text = text
            comment.save()
            return UpdateComment(comment=comment)
        return UpdateComment(comment=None)


class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    comment = graphene.Field(CommentType)

    @classmethod
    def mutate(cls, root, info, id):
        comment = Comment.objects.get(pk=id)
        comment.delete()
        return None


class LikePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        data = LikePostInput(required=True)

    @classmethod
    def mutate(cls, root, info, data=None):
        user = User.objects.get(username=data.user.username)
        post = Post.objects.get(id=data.post.id)
        post.users_who_liked.add(user)
        return LikePost(post=post)


class LikeComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        data = LikeCommentInput(required=True)

    @classmethod
    def mutate(cls, root, info, data=None):
        user = User.objects.get(username=data.user.username)
        comment = Comment.objects.get(id=data.comment.id)
        comment.users_who_liked.add(user)
        return LikePost(comment=comment)
