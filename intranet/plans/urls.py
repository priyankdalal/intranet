from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add-plan',views.addPlan,name='add-plan'),
]