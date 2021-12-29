from django.db import models

# Create your models here.


class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=20)

    def __str__(self):
        return self.deptname


class Emp(models.Model):
    ch = [
        ('m', 'Male'),
        ('f', 'Female')
    ]
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=ch)

    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

    salary = models.IntegerField(null=True)
