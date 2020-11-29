# Generated by Django 3.1.2 on 2020-11-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20201128_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employecreation',
            name='designation',
            field=models.CharField(choices=[('se', 'Software Engineer'), ('te', 'Test Engineer'), ('dp', 'Devoleper'), ('ba', 'Bussiness Analyst'), ('ae', 'AI Engineer'), ('dev', 'Devops Engineer')], max_length=100, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='employecreation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='employecreation',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Phone'),
        ),
    ]
