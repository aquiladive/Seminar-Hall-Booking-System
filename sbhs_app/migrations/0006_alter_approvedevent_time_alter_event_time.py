# Generated by Django 5.0.7 on 2024-07-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbhs_app', '0005_approvedevent_event_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedevent',
            name='time',
            field=models.CharField(choices=[('9AM-1PM', '9 AM - 1 PM'), ('1PM-5PM', '1 PM - 5 PM')], default=('9AM-1PM', '9 AM - 1 PM'), max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(choices=[('9AM-1PM', '9 AM - 1 PM'), ('1PM-5PM', '1 PM - 5 PM')], default=('9AM-1PM', '9 AM - 1 PM'), max_length=10),
        ),
    ]
