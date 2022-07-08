from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")

class Tes(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")

class Tes2(models.Model):
    question_text2 = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")