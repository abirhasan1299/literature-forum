from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class comment(models.Model):

    username = models.CharField(max_length=500)
    fullname = models.CharField(max_length=500)
    cmt = models.TextField(max_length=5000)
    date_time = models.DateTimeField()
    poem_unique_id = models.IntegerField()

    def __str__(self):
        return self.username
    
class Poem(models.Model):
    category = (
        ("কিশোর","কিশোর"),
        ("রোম্যান্টিক","রোম্যান্টিক"),
        ("আঠারো উর্ধ্ব","আঠারো উর্ধ্ব"),
        ("ভালোবাসা-প্রেম","ভালোবাসা-প্রেম"),
        ("দুঃখের কবিতা","দুঃখের কবিতা"),
        ("জাগরন মূলক","জাগরন মূলক"),
        ("সমাজকেন্দ্রিক","সমাজকেন্দ্রিক"),
        ("দেশাত্মবোধক","দেশাত্মবোধক"),
        ("প্রকৃতিপ্রেম","প্রকৃতিপ্রেম"),
        ("শিশু কবিতা","শিশু কবিতা")
    )
    author = models.CharField(max_length=1000)
    unique_id = models.ForeignKey(User,on_delete=models.CASCADE)
    poem_name = models.CharField(max_length=5000)
    poem_description = models.TextField(max_length=1000000)
    view = models.IntegerField()
    date = models.DateTimeField()
    tag = models.CharField(max_length=1000,choices=category)

    def __str__(self):
        return self.poem_name
    
