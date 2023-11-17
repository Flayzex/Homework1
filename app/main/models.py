from django.db import models

# Create your models here.
class Words(models.Model):
    word1 = models.CharField(max_length=255)
    word2 = models.CharField(max_length=255)