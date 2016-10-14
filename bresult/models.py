from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name

class Result(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.SET_NULL, related_name="person", null=True, blank=True)
    number = models.IntegerField()
    result = models.IntegerField()
#    tournament_round = models.IntegerField();

class Tournament(models.Model):
    round = models.IntegerField()
#    cmd_next_round = models.IntegerField()
	
    def nextRound(self,a):
        self.round = a	
