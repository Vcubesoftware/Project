from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Employee
from django.contrib import messages
from .forms import EmpForm, CreateUser

# Create your views here.


def register(request):
    form = CreateUser()

    if request.method == "POST":

        obj = CreateUser(request.POST)
        print(request.POST)
        if obj.is_valid():
            obj.save()

            return render(request, 'login.html')
        else:
            return render(request, 'register.html')

    context = {'userform': form}
    return render(request, 'register.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def empDetails(request):

    # return HttpResponse(' I this is my first response')

    emp = EmpForm()
    try:
        print(request.POST)
        if request.method == 'POST':
            '''eno = request.POST['no']
            ename = request.POST['name']
            salary = request.POST['salary']
            print('Creating object')
            emp = Employee.objects.create(
                empno=eno, empname=ename, salary=salary)

            print(emp)

            print(eno, ename, salary) '''

            #obj = EmpForm(request.POST)

            # if obj.is_valid():

            #  obj.save()

            eForm = EmpForm(request.POST)

            if eForm.is_valid():
                emp = Employee()
                emp.empno = eForm.cleaned_data['empno']
                emp.empname = eForm.cleaned_data['empname']
                emp.salary = eForm.cleaned_data['salary']
                emp.joining_date = eForm.cleaned_data['joining_date']

                emp.save()

                messages.success(request, 'Successfully inserted')

    except Exception:
        messages.error(request, 'Something went wrong')
        messages.info(request, 'It is looking like primary key issue')

    return render(request, 'empdetails.html', {'form': emp, })


def fetchData(request):

    # if request.method == 'POST':

    if request.method == 'GET':
        return render(request, 'search.html')

    elif 'all' in request.POST:

        data = Employee.objects.all()

        context = {
            'info': data
        }

        return render(request, 'output.html', context)
    else:
        eno = request.POST['sno']

        data = Employee.objects.filter(empno=eno)

        context = {
            'info': data
        }

        print(context)
        return render(request, 'output.html', context)


def deleteEmp(request):

    if request.method == 'POST':
        no = request.POST['eno']

        Employee.objects.delete(empno=no)

    return render(request, 'delete.html')


def userLogin(request):
    if request.method == 'POST':
        user = request.POST['user']
        pwd = request.POST['pwd']

        # authenticate(request,*args,**kwargs)
        valid = authenticate(request, username=user, password=pwd)
        # print(valid)

        if valid is not None:
            # login(request)
            login(request, valid)

            return render(request, 'home.html')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def userLogout(request):

    if request.user.is_authenticated:
        logout(request)
        return render(request, 'login.html')
    else:
        return render(request, 'home.html')
