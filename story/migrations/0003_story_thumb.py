# Generated by Django 4.2.4 on 2023-09-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_alter_story_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='thumb',
            field=models.ImageField(default=123, upload_to='thumbnails/'),
            preserve_default=False,
        ),
    ]
