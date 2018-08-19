from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add-router',views.addRouter,name="add-router"),
    path('remove-router',views.removeRouter,name="remove-router"),
]