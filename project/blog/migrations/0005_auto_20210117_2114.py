# Generated by Django 3.1.4 on 2021-01-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210117_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='content',
            field=models.TextField(max_length=250),
        ),
    ]