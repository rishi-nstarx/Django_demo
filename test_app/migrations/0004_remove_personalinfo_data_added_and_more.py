# Generated by Django 5.0.7 on 2024-07-12 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_alter_personalinfo_data_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='data_added',
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 12, 36, 2, 139606, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='infocertificate',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 12, 36, 2, 141346, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='inforeview',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 12, 36, 2, 140060, tzinfo=datetime.timezone.utc)),
        ),
    ]
