from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)

    def _str_(self):
        return self.name + ' ' + self.surname


class User (models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=225)
