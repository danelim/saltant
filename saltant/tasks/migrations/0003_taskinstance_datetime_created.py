# Generated by Django 2.0.6 on 2018-06-24 02:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20180624_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskinstance',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
