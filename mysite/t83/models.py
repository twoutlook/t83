from django.db import models

# Create your models here.
class T83(models.Model):
    t83_num = models.CharField(max_length=2)
    t83_name = models.CharField(max_length=30)
    t83_short = models.CharField(max_length=4)
