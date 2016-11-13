from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL, related_name="person", null=True, blank=True)
    database = models.IntegerField()

    def __str__(self):
        return self.user.last_name

class Pair(models.Model):
    id = models.IntegerField(primary_key = True)
    person1 = models.ForeignKey(Person,on_delete=models.SET_NULL, related_name="person1", null=True, blank=True)
    person2 = models.ForeignKey(Person,on_delete=models.SET_NULL, related_name="person2", null=True, blank=True)

    def __str__(self):
        return str(self.person1) +"+"+str(self.person2)

class Team(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    pair1 = models.ForeignKey(Pair,on_delete=models.SET_NULL, related_name="pair1", null=True, blank=True)
    pair2 = models.ForeignKey(Pair,on_delete=models.SET_NULL, related_name="pair2", null=True, blank=True)


class Tournament(models.Model):
    round = models.IntegerField()

    def __str__(self):
        return str(self.round)

