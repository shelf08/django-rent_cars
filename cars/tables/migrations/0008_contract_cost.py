# Generated by Django 5.1.2 on 2024-12-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_remove_contract_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
