# Generated by Django 3.2.12 on 2022-03-15 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentPost',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commentUser',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='postCategory',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='categoryThrough',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='postThrough',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]
