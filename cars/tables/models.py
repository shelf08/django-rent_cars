from django.db import models

class Automobile(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Automobile'

    def __str__(self):
        return self.brand




class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    years = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'Client'

    def __str__(self):
        return self.name


class Club_card(models.Model):
    bonuses = models.IntegerField()
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)


    class Meta:
        db_table = 'Club_card'

    def str(self):
        return f'{self.bonuses} бонусов у {self.client.name}'



class Contract(models.Model):
    contract = models.CharField(max_length=100, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField()
    time_start = models.TimeField()
    time_finsh = models.TimeField()
    automobile = models.ForeignKey(to=Automobile, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты';
        db_table = 'Контракт'

    def __str__(self):
        return self.contract