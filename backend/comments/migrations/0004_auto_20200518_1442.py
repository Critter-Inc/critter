# Generated by Django 3.0.6 on 2020-05-18 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_member_since'),
        ('comments', '0003_auto_20200517_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.User'),
        ),
    ]
