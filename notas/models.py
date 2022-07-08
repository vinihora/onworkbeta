from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")

class Answer(models.Model):
    answer_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")