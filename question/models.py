from django.db import models
from random import randint
from theme.models import Theme

# Create your models here.

class Question(models.Model):
    id = models.AutoField(primary_key=True)

    theme = models.ForeignKey(Theme, related_name='questions')

    question = models.CharField(max_length = 500)

    answer1 = models.CharField(max_length = 500)
    answer2 = models.CharField(max_length = 500)
    answer3 = models.CharField(max_length = 500)
    answer4 = models.CharField(max_length = 500)

    right_answer = models.IntegerField()