# Generated by Django 3.2.6 on 2021-11-22 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ra', '0004_auto_20211122_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group_bookmark',
            old_name='is_trash',
            new_name='is_removed',
        ),
        migrations.AddField(
            model_name='bookmark_folder',
            name='is_removed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookmark_folder',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 69025)),
        ),
        migrations.AlterField(
            model_name='folder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 68026)),
        ),
        migrations.AlterField(
            model_name='group',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 67025)),
        ),
        migrations.AlterField(
            model_name='group_bookmark',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 68026)),
        ),
        migrations.AlterField(
            model_name='practice',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 70025)),
        ),
        migrations.AlterField(
            model_name='site',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 69025)),
        ),
        migrations.AlterField(
            model_name='user_access',
            name='date_of_access',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 70025)),
        ),
        migrations.AlterField(
            model_name='user_bookmark',
            name='dateAccessed',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 65016)),
        ),
        migrations.AlterField(
            model_name='user_bookmark',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 10, 21, 65016)),
        ),
    ]
