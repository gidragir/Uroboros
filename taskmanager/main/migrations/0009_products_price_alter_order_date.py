# Generated by Django 4.0.3 on 2022-04-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
