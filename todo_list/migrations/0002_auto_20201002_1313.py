# Generated by Django 3.1.1 on 2020-10-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
