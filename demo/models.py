from django.db import models

# Create your models here.
class school(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    img_name = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
    