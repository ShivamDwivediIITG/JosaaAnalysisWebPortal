from django.db import models

# Create your models here.
class rec(models.Model):
    institute = models.CharField(max_length=255)
    academic = models.CharField(max_length=255)
    quota = models.CharField(max_length=2)
    seattype = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    openingrank = models.IntegerField()
    closingrank = models.IntegerField()
    year = models.IntegerField()
    round = models.IntegerField()
    def __str__(self):
        return self.institute