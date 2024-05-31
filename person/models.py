from django.db import models
from django.contrib.auth.models import User

class person(models.Model):

    r_s = (
        ('একাকী','একাকী'),
        ('বিবাহিত','বিবাহিত'),
        ('তালাকপ্রাপ্ত','তালাকপ্রাপ্ত'),
        ('জটিল','জটিল'),
        ('পৃথক','পৃথক'),
        ('দেহ-বিলাসী','দেহ-বিলাসী')
    )

    tags = (
        ('গল্পকার','গল্পকার'),
        ('কবি','কবি'),
        ('ঔপন্যাসিক','ঔপন্যাসিক'),
        ('কথাসাহিত্যিক','কথাসাহিত্যিক'),
        ('গানলেখক','গানলেখক'),
        ('প্রাবন্ধিক','প্রাবন্ধিক'),
        ('দার্শনিক','দার্শনিক')
    )
    e_q = (
        ('B.Sc','B.Sc'),
        ('B.Com','B.Com'),
        ('BBA','BBA'),
        ('HSC','HSC'),
        ('SSC','SSC'),
        ('PSC','PSC'),
        ('PSC', 'পড়ালেখা নাই')
    )
    gen =(
        ('ছেলে','ছেলে'),
        ('মেয়ে','মেয়ে'),
        ('উভলিঙ্গ','উভলিঙ্গ'),
    )
    nickname = models.CharField(max_length=500)
    gender = models.CharField(max_length=500,choices=gen)
    death = models.CharField(max_length=500)
    unique_id = models.ForeignKey(User,on_delete=models.CASCADE)

    bio = models.TextField(max_length=5000000)
    mobile = models.IntegerField()

    relationship_status = models.CharField(max_length=500,choices=r_s)

    tags_1 = models.CharField(max_length=500,choices=tags)
    tags_2 = models.CharField(max_length=500,choices=tags)
    tags_3 = models.CharField(max_length=500,choices=tags)

    profession = models.CharField(max_length=500)
    fav_clr = models.CharField(max_length=50)

#-----------Educational Qualification Test-------------

    edu_qual = models.CharField(max_length=500,choices=e_q)
    edu_ins = models.CharField(max_length=500)
    depart_sub = models.CharField(max_length=500)

    dob = models.DateField()

#----------Social Media Link ------------

    fb = models.CharField(max_length=5000)
    youtube = models.CharField(max_length=5000)
    insta = models.CharField(max_length=5000)
#------------------Qr Code Generator--------------
    qr_code_name = models.CharField(max_length=10000000)

    def __str__(self):
        return self.nickname
    
