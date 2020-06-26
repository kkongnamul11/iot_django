from django.db import models

# Create your models here.

# 온습도 데이터베이스
class Temperature(models.Model):
    temp = models.IntegerField()
    humi = models.IntegerField()