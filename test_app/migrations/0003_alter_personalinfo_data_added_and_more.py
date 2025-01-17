# Generated by Django 5.0.7 on 2024-07-12 12:30

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_personalinfo_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='data_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 12, 30, 42, 132079, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='description',
            field=models.TextField(default='No Descriptions'),
        ),
        migrations.CreateModel(
            name='InfoCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certifiacte_number', models.CharField(max_length=100)),
                ('issue_date', models.DateTimeField(default=datetime.datetime(2024, 7, 12, 12, 30, 42, 134471, tzinfo=datetime.timezone.utc))),
                ('valid_until', models.DateTimeField()),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='test_app.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='InfoReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2024, 7, 12, 12, 30, 42, 132797, tzinfo=datetime.timezone.utc))),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='test_app.personalinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plateform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('infos', models.ManyToManyField(related_name='plateform', to='test_app.personalinfo')),
            ],
        ),
    ]
