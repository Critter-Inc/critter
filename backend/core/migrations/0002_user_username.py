# Generated by Django 3.0.5 on 2020-05-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='No username set.', max_length=50, null=True),
        ),
    ]
