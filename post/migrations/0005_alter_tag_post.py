# Generated by Django 4.2 on 2023-07-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_tag_post_tag_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(related_name='tags', to='post.post'),
        ),
    ]