from django.db import models
import datetime

# Create your models here.
class clues(models.Model):
    ques_id = models.PositiveIntegerField(blank=True, null=True, unique=True)
    prev_ans = models.CharField(max_length = 50, null = True, blank = True)
    question = models.CharField(max_length = 100, blank = True, null = True)
    ans = models.CharField(max_length = 50, null = True, blank = True)

class users(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    team_id = models.PositiveIntegerField(unique=True,blank=True, null=True)
    created = models.DateTimeField(default= datetime.datetime.now())