from django.forms import forms, ModelForm
from django.forms import TextInput,NumberInput,EmailInput,Select
from .models import EmployeCreation

class EmployeCreationForm(ModelForm):
    class Meta:
        model = EmployeCreation
        fields = '__all__'

        widgets={
            'name': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'designation': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'address': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }