# Generated by Django 2.1.4 on 2019-01-19 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.IntegerField(),
        ),
    ]