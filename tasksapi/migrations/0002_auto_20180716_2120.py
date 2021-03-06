# Generated by Django 2.0.6 on 2018-07-16 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinstance',
            name='state',
            field=models.CharField(choices=[('created', 'created'), ('published', 'published'), ('running', 'running'), ('successful', 'successful'), ('failed', 'failed'), ('terminated', 'terminated')], default='created', max_length=10),
        ),
        migrations.AlterField(
            model_name='tasktype',
            name='container_type',
            field=models.CharField(choices=[('docker', 'Docker'), ('singularity', 'Singularity')], help_text='The type of container provided', max_length=11),
        ),
    ]
