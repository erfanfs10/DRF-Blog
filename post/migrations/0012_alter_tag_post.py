# Generated by Django 4.2 on 2023-07-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_save'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='tags', related_query_name='tags', to='post.post'),
        ),
    ]
