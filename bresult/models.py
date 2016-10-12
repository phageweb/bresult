from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name

class Result(models.Model):
    person = models.ForeignKey(Person)
    number = models.IntegerField()
    result = models.IntegerField()


