# Generated by Django 3.0.3 on 2020-06-28 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]