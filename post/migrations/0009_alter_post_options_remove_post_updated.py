# Generated by Django 4.2 on 2023-07-14 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_post_options_alter_post_view'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created', '-view')},
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
    ]