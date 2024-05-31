from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class story(models.Model):
    tag = (
        ('রোম্যান্টিক','রোম্যান্টিক'),
        ('সামাজিক','সামাজিক'),
        ('প্রকৃতি ও মানুষ','প্রকৃতি ও মানুষ'),
        ('কাল্পনিক ও অতিপ্রাকৃত','কাল্পনিক ও অতিপ্রাকৃত'),
        ('প্রতীকধর্মী','প্রতীকধর্মী'),
        ('আঠারো উর্ধ্ব','আঠারো উর্ধ্ব'),
        ('বৈজ্ঞানিক','বৈজ্ঞানিক'),
        ('মনস্তাত্তিক','মনস্তাত্তিক'),
        ('ঐতিহাসিক','ঐতিহাসিক'),
        ('কমেডি','কমেডি'),
        ('বাস্তব','বাস্তব'),
        ('ডিটেকিভ','ডিটেকিভ'),
        ('ঘরোয়া','ঘরোয়া'),
        ('ভ্রমণ কাহিনী','ভ্রমণ কাহিনী'),
        ('শুধু গল্প','শুধু গল্প')
    )
    title = models.CharField(max_length=5000)
    tag = models.CharField(max_length=500,choices=tag)
    description = models.TextField(max_length=500000000000000)
    unique_id = models.ForeignKey(User,on_delete=models.CASCADE)
    author = models.CharField(max_length=500)
    view = models.IntegerField(default=0)
    thumb = models.ImageField(upload_to='thumbnails/')
    
    def __str__(self):
        return self.title
    
    