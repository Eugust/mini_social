import graphene
from graphene_django import DjangoObjectType

from posts.models import Post, Comment
from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'phone',
            'gender'
        )


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'pub_date',
            'author',
            'likes'
        )

    likes = graphene.Int()

    def resolve_likes(self, info):
        return self.users_who_liked.count()


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'author',
            'created',
            'text',
            'likes'
        )

    likes = graphene.Int()

    def resolve_likes(self, info):
        return self.users_who_liked.count()
