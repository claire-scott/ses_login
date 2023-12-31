# Generated by Django 3.1.2 on 2023-06-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='event_category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='event_type',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_number',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='unit',
            name='linking_key',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='unit',
            name='postcode',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
