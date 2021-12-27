from django.urls import path
from . import views

urlpatterns = [
    path('', views.userLogin, name='login'),
    path('login', views.userLogin, name='login'),
    path('logout', views.userLogout),
    path('home', views.home, name='home'),
    # path('', views.empDetails, name='empDetails'),
    path('input', views.empDetails, name='inputdata'),
    path('output', views.fetchData),
    path('delete', views.deleteEmp),
    # path('register', views.register),
    path('register', views.RegisterView.as_view(), name='register'),
    path('all', views.AllData.as_view(), name='fetchall')

]
