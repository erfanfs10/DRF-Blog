# Generated by Django 4.2 on 2023-07-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_remove_tag_post_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
