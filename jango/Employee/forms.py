from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Employee


'''class EmpForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  '''


class EmpForm(Form):
    empno = forms.IntegerField()
    empname = forms.CharField(max_length=10)
    salary = forms.IntegerField()
    joining_date = forms.DateField(widget=forms.SelectDateWidget)


class CreateUser(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']
