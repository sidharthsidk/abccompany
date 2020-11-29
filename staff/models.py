from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

class EmployeCreation(models.Model):

    id = models.BigAutoField(
        primary_key=True,
    )
    DESIG = (
        ('se','Software Engineer'),
        ('te','Test Engineer'),
        ('dp','Devoleper'),
        ('ba','Bussiness Analyst'),
        ('ae','AI Engineer'),
        ('dev','Devops Engineer')
    )

    name = models.CharField(
        verbose_name="Employee Name",
        max_length=100,
        unique=False,
        null=False,
        blank=False,
    )
    designation = models.CharField(
        verbose_name="Designation",
        max_length=100,
        unique=False,
        null=False,
        blank=False,
        choices=DESIG
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True
    )
    email = models.EmailField(
        verbose_name="Email",
        blank=False,
        null=False
    )
    phone = models.CharField(
        verbose_name="Phone",
        max_length=10,
        blank=False,
        null=False       
    )
    address = models.CharField(
        verbose_name="Address",
        max_length=50,
        blank=False,
        null=False       
    )
