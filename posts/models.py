from django.db import models

from users.models import User


class Post(models.Model):
    text = models.TextField(
        verbose_name="Post",
        help_text="Create post"
    )
    pub_date = models.DateTimeField(
        verbose_name="Data published",
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    users_who_liked = models.ManyToManyField(
        User,
        related_name="users_who_liked_post",
        blank=True
    )


    class Meta:
        ordering = ["-pub_date"]

    def __str__(self) -> str:
        return self.text[:20]


class Comment(models.Model):
    text = models.TextField(
        verbose_name="Comments",
        help_text="Add a comment"
    )
    created = models.DateTimeField(
        verbose_name="Data created",
        auto_now_add=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    users_who_liked = models.ManyToManyField(
        User,
        related_name="users_who_liked_comment",
        blank=True
    )


    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return "{} comments to {}".format(self.author, self.post)
