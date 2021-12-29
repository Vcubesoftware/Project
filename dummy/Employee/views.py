from django.shortcuts import render
from django.http import HttpResponse
from .models import Emp, Dept
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Sum, Count, Max, Min

# Create your views here.


def first(request):

    # result = Emp.objects.all()
    # result = Emp.objects.filter(empname__exact='Veeranji')
    # result = Emp.objects.filter(empname__startswith='R')
    # result = Emp.objects.filter(salary__gt=60000)  # select * from Emp where salary>60000;
    # result = Emp.objects.filter(salary__gt=60000)
    # result = Emp.objects.filter(empname__icontains='e')
    # result = Emp.objects.filter(
    #   Q(empname__startswith='R') | Q(salary__gt=40000))
    try:

        #result = Emp.objects.get(salary__gt=40000)
        #result = Emp.objects.exclude(empname__startswith='V')
        # print(result)
        # for i in result:
        #   print(i.empname, i.salary)

        #result = Emp.objects.aggregate(Max('salary'))
        # print(result)

        # Emp.objects.values('')
        #results = Emp.objects.filter(dept__deptname='Development')
        # print(results)

        results = Emp.objects.values('dept').annotate(Sum('salary'))
        print(results)

        # for i in results:
        #   print(i.empname, i.salary)
    except MultipleObjectsReturned:
        return HttpResponse('Something went wrong')
    return HttpResponse('I am dummy app')
