# Generated by Django 3.1.3 on 2020-11-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]
