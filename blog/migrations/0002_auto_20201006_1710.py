# Generated by Django 3.0.6 on 2020-10-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='post_image',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Type something', max_length=300),
        ),
    ]
