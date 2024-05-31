# Generated by Django 4.2.4 on 2023-09-06 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('ছেলে', 'ছেলে'), ('মেয়ে', 'মেয়ে'), ('উভলিঙ্গ', 'উভলিঙ্গ')], max_length=500)),
                ('t_story', models.IntegerField()),
                ('t_poem', models.IntegerField()),
                ('t_novel', models.IntegerField()),
                ('efficiency', models.IntegerField()),
                ('badge', models.CharField(max_length=500)),
                ('bio', models.TextField(max_length=5000000)),
                ('mobile', models.IntegerField()),
                ('relationship_status', models.CharField(choices=[('একাকী', 'একাকী'), ('বিবাহিত', 'বিবাহিত'), ('তালাকপ্রাপ্ত', 'তালাকপ্রাপ্ত'), ('জটিল', 'জটিল'), ('পৃথক', 'পৃথক'), ('দেহ-বিলাসী', 'দেহ-বিলাসী')], max_length=500)),
                ('tags_1', models.CharField(choices=[('গল্পকার', 'গল্পকার'), ('কবি', 'কবি'), ('ঔপন্যাসিক', 'ঔপন্যাসিক'), ('কথাসাহিত্যিক', 'কথাসাহিত্যিক'), ('গানলেখক', 'গানলেখক'), ('প্রাবন্ধিক', 'প্রাবন্ধিক'), ('দার্শনিক', 'দার্শনিক')], max_length=500)),
                ('tags_2', models.CharField(choices=[('গল্পকার', 'গল্পকার'), ('কবি', 'কবি'), ('ঔপন্যাসিক', 'ঔপন্যাসিক'), ('কথাসাহিত্যিক', 'কথাসাহিত্যিক'), ('গানলেখক', 'গানলেখক'), ('প্রাবন্ধিক', 'প্রাবন্ধিক'), ('দার্শনিক', 'দার্শনিক')], max_length=500)),
                ('tags_3', models.CharField(choices=[('গল্পকার', 'গল্পকার'), ('কবি', 'কবি'), ('ঔপন্যাসিক', 'ঔপন্যাসিক'), ('কথাসাহিত্যিক', 'কথাসাহিত্যিক'), ('গানলেখক', 'গানলেখক'), ('প্রাবন্ধিক', 'প্রাবন্ধিক'), ('দার্শনিক', 'দার্শনিক')], max_length=500)),
                ('tags_4', models.CharField(choices=[('গল্পকার', 'গল্পকার'), ('কবি', 'কবি'), ('ঔপন্যাসিক', 'ঔপন্যাসিক'), ('কথাসাহিত্যিক', 'কথাসাহিত্যিক'), ('গানলেখক', 'গানলেখক'), ('প্রাবন্ধিক', 'প্রাবন্ধিক'), ('দার্শনিক', 'দার্শনিক')], max_length=500)),
                ('profession', models.CharField(max_length=500)),
                ('fav_clr', models.CharField(max_length=50)),
                ('edu_qual', models.CharField(choices=[('B.Sc', 'B.Sc'), ('B.Com', 'B.Com'), ('BBA', 'BBA'), ('HSC', 'HSC'), ('SSC', 'SSC'), ('PSC', 'PSC'), ('পড়ালেখা নাই', 'পড়ালেখা নাই')], max_length=500)),
                ('edu_ins', models.CharField(max_length=500)),
                ('depar_sub', models.CharField(max_length=500)),
                ('dob', models.DateField()),
                ('fb', models.CharField(max_length=5000)),
                ('youtube', models.CharField(max_length=5000)),
                ('insta', models.CharField(max_length=5000)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
