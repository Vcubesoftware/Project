from django.db import models

# Create your models here.


class Employee(models.Model):
    empno = models.IntegerField(null=True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.empname
