# Generated by Django 3.0.6 on 2020-05-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('core', '0010_auto_20200519_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(default='member', to='auth.Group'),
        ),
    ]
