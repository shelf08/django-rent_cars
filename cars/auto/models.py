from django.db import models


class Auto(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    clas = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.clas})"