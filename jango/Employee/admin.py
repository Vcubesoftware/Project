from django.contrib import admin
from django.db.models import fields
from .models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    # class Meta:
    #model = Employee
    #fields = ('empname', 'empno', 'salary')
    list_display = ['empname', 'salary', 'salEvalution', 'bonus']
    ordering = ['-empname']

    def salEvalution(self, irfan):
        if irfan.salary > 70000:
            return 'High'
        else:
            return 'Low'

    def bonus(self, obj):
        return obj.salary/10


admin.site.register(Employee, EmployeeAdmin)
