# Generated by Django 5.1.2 on 2024-12-03 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_remove_contract_contract_id_alter_automobile_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='time_finsh',
            new_name='time_finish',
        ),
    ]
