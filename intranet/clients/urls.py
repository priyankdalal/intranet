# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('add-client',views.addClient,name="add-client"),
]

