# Generated by Django 3.1.2 on 2023-06-15 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0003_userunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='event_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
