# Generated by Django 3.0.6 on 2020-05-17 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biz', '0017_auto_20200517_1152'),
        ('comments', '0002_auto_20200504_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='biz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='biz.Biz'),
        ),
    ]
