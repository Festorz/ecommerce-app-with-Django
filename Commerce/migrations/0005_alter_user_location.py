# Generated by Django 3.2.2 on 2021-05-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commerce', '0004_auto_20210509_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]