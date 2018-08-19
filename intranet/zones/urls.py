# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns=[
        path('',views.index,name="index"),
        path('add-zone',views.addZone,name="add-zone"),
        path('remove-zone',views.removeZone,name="remove-zone"),
]
