# Generated by Django 3.1.2 on 2020-10-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(max_length=100),
        ),
    ]
