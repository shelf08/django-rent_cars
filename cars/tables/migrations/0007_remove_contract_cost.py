# Generated by Django 5.1.2 on 2024-12-03 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_rename_time_finsh_contract_time_finish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='cost',
        ),
    ]