# Generated by Django 3.2.3 on 2021-05-20 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventapp', '0006_rename_user_usercreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinevent',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='usercreated',
        ),
    ]
