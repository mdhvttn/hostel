from django.db import models

# Create your models here.

class Year(models.Model):

    year = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.year)


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.IntegerField(unique=True)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.name











