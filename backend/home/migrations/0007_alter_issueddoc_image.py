# Generated by Django 4.1.7 on 2023-07-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_issueddoc_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueddoc',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
