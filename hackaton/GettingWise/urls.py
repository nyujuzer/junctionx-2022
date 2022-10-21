from django.urls import path
from GettingWise import views

app_name = 'GettingWise'

urlpatterns = [
    path('', views.index, name='index'),
]
