# Generated by Django 4.0.3 on 2022-04-16 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 22, 54, 45, 35650)),
        ),
    ]