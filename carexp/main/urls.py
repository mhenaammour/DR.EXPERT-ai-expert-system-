from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('expertpage', views.expertpage,name='expertpage'),
    path('symptom_checker', views.symptom_checker,name='symptom_checker')
]
