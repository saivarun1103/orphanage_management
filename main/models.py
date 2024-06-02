from django.db import models

class Orphan(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
