# Generated by Django 3.0.5 on 2020-05-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biz', '0003_openinghours'),
    ]

    operations = [
        migrations.AddField(
            model_name='biz',
            name='from_hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='biz',
            name='to_hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='biz',
            name='weekday',
            field=models.IntegerField(blank=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='OpeningHours',
        ),
    ]
