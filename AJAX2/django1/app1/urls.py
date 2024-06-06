from django.urls import path
from app1.views import home,api1,api2
urlpatterns=[path('',home),
             path('api1',api1),
             path('api2',api2)]