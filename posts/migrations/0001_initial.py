# Generated by Django 4.0.1 on 2022-01-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Add a comment', verbose_name='Comments')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data created')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Create post', verbose_name='Post')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Data published')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
