# Generated by Django 3.1.1 on 2020-10-05 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_list', '0004_auto_20201005_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
