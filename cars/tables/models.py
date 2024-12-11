from django.db import models
from decimal import Decimal
from datetime import datetime
from django.core.exceptions import ValidationError


# from django.contrib import admin
# from .widgets import Time30MinInput
class Automobile(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:

        db_table = 'Automobile'

    def __str__(self):
        return f"{self.id}. {self.brand} {self.model}"




class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    years = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)
        # Создаем клубную карту с привязкой к этому клиенту
        Club_card.objects.create(client=self, bonuses=0)

    class Meta:

        db_table = 'Client'
    def __str__(self):
        return f"{self.id}. {self.name} {self.phone_number}"



class Club_card(models.Model):
    bonuses = models.IntegerField(default=0)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)


    class Meta:

        db_table = 'Club_card'

    def __str__(self):
        return f"{self.id}. {self.bonuses} бонусов у клиента {self.client.id}"



class Contract(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField()
    time_start = models.TimeField()
    time_finish = models.TimeField()
    automobile = models.ForeignKey(to=Automobile, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Вычисляем стоимость контракта
        if self.time_finish and self.time_start:
            # Вычисляем общее время аренды в минутах
            start = datetime.combine(self.date, self.time_start)
            finish = datetime.combine(self.date, self.time_finish)
            duration = (finish - start).total_seconds() / 60  # Время в минутах

            # Проверяем, что время аренды положительное
            if duration < 0:
                raise ValidationError("Время окончания должно быть позже времени начала.")

            # Вычисляем количество 30-минутных интервалов
            intervals = duration // 30

            # Умножаем количество интервалов на стоимость автомобиля (преобразуем стоимость в Decimal)
            total_cost = Decimal(intervals) * self.automobile.cost

            # Устанавливаем рассчитанную стоимость контракта
            self.cost = total_cost

        # Вызываем метод родительского класса для сохранения контракта
        super(Contract, self).save(*args, **kwargs)

        # Обновляем бонусы клиента
        self.update_client_bonuses()

    def update_client_bonuses(self):
        # Вычисляем количество бонусов (10% от стоимости контракта)
        bonuses_to_add = int(self.cost / 10)

        # Ищем либо создаем клубную карту клиента
        club_card, created = Club_card.objects.get_or_create(client=self.client)

        # Обновляем количество бонусов
        club_card.bonuses += bonuses_to_add
        club_card.save()

    class Meta:

        db_table = 'Contract'

    def __str__(self):
        return f"Договор номер {self.id} для клиента {self.client.name}"



# class ContractAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         Contract.time_start: {'widget': Time30MinInput()},
#         Contract.time_finish: {'widget': Time30MinInput()},
#     }
#
# admin.site.register(Contract, ContractAdmin)