# Generated by Django 2.0.5 on 2022-02-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop_yield', '0010_auto_20220210_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop_yield_data',
            name='production',
            field=models.IntegerField(),
        ),
    ]
