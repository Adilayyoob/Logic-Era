# Generated by Django 3.2.3 on 2021-05-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_joinevent_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinevent',
            name='status',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Joined', 'Joined'), ('Not Joined', 'Not Joined')], max_length=200, null=True),
        ),
    ]
