# Generated by Django 3.1.2 on 2020-11-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeCreation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('email', models.EmailField(max_length=170, verbose_name='Email')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
            ],
        ),
    ]