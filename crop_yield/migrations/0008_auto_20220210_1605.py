# Generated by Django 2.0.5 on 2022-02-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop_yield', '0007_dist_soil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop_yield_data',
            name='production',
            field=models.IntegerField(max_length=300),
        ),
    ]
