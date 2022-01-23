from django.contrib import admin

from .models import Post, Comment


class PostLikeLine(admin.TabularInline):
    model = Post.users_who_liked.through
    extra = 1


class CommentLikeLine(admin.TabularInline):
    model = Comment.users_who_liked.through
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'pub_date')
    inlines = (PostLikeLine,)
    search_fields = ('author',)
    exclude = ('users_who_liked',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'post', 'created')
    inlines = (CommentLikeLine,)
    search_fields = ('author',)
    exclude = ('users_who_liked',)
