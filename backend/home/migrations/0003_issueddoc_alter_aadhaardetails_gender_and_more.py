# Generated by Django 4.1.7 on 2023-07-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_aadhaardetails_pandetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.TextField(max_length=12)),
                ('card_no', models.CharField(max_length=12)),
                ('dob', models.DateField()),
                ('image', models.FileField(upload_to='upload/images')),
            ],
        ),
        migrations.AlterField(
            model_name='aadhaardetails',
            name='gender',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='aadhaardetails',
            name='image',
            field=models.FileField(upload_to='upload/images'),
        ),
        migrations.AlterField(
            model_name='pandetails',
            name='image',
            field=models.FileField(upload_to='upload/images'),
        ),
    ]