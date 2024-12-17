# Generated by Django 5.1.2 on 2024-12-17 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_alter_club_card_bonuses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_card',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_card', to='tables.client'),
        ),
    ]
