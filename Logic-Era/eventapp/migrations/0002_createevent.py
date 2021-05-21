# Generated by Django 3.2.3 on 2021-05-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='createevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('date', models.DateTimeField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('max', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=2500, null=True)),
                ('banner', models.CharField(max_length=2500, null=True)),
                ('user', models.IntegerField(null=True)),
            ],
        ),
    ]
