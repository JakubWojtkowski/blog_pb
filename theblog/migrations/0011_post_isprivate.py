# Generated by Django 4.2.13 on 2024-06-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_rename_text_comment_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isPrivate',
            field=models.BooleanField(default=False),
        ),
    ]
