# Generated by Django 3.2.6 on 2021-11-20 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ra', '0002_auto_20211120_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark_folder',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 472004)),
        ),
        migrations.AlterField(
            model_name='folder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 471014)),
        ),
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 470014)),
        ),
        migrations.AlterField(
            model_name='group_bookmark',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 471014)),
        ),
        migrations.AlterField(
            model_name='practice',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 475004)),
        ),
        migrations.AlterField(
            model_name='site',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 472004)),
        ),
        migrations.AlterField(
            model_name='user_access',
            name='date_of_access',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 473016)),
        ),
        migrations.AlterField(
            model_name='user_bookmark',
            name='dateAccessed',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 469002)),
        ),
        migrations.AlterField(
            model_name='user_bookmark',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 20, 40, 37, 469002)),
        ),
    ]
