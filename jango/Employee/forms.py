from django import forms
from django.forms import ModelForm, Form

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
