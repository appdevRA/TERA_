# Generated by Django 3.2.6 on 2021-11-20 11:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookmark_folder',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 810739)),
        ),
        migrations.AlterField(
            model_name='folder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 810739)),
        ),
        migrations.AlterField(
            model_name='group',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 809739)),
        ),
        migrations.AlterField(
            model_name='group_bookmark',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 810739)),
        ),
        migrations.AlterField(
            model_name='practice',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 812739)),
        ),
        migrations.AlterField(
            model_name='site',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 811739)),
        ),
        migrations.AlterField(
            model_name='user_access',
            name='date_of_access',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 811739)),
        ),
        migrations.AlterField(
            model_name='user_bookmark',
            name='dateAccessed',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 807724)),
        ),
        migrations.AlterField(
            model_name='user_bookmark',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 19, 51, 26, 807724)),
        ),
    ]
