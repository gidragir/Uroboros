# Generated by Django 4.0.3 on 2022-03-31 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_productmove_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='desription',
            field=models.TextField(default='SOME STRING', max_length=1024),
        ),
    ]
