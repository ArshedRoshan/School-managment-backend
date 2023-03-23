from django.db import models

# Create your models here.
class grade(models.Model):
    classes = models.CharField(max_length=50,primary_key=True)
