# Generated by Django 4.2.4 on 2023-09-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_remove_person_badge_remove_person_efficiency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='death',
            field=models.CharField(default=12, max_length=500),
            preserve_default=False,
        ),
    ]
