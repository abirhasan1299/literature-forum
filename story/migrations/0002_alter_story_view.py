# Generated by Django 4.2.4 on 2023-09-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
