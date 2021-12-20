from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.empDetails, name='empDetails'),
    path('input', views.empDetails, name='inputdata'),
    path('output', views.fetchData),
    path('delete', views.deleteEmp)

]
