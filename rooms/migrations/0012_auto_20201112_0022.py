# Generated by Django 3.1.3 on 2020-11-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_auto_20201108_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_phtos'),
        ),
    ]
