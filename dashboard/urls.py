from calendar import c
from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path("", views.index, name='dashboard-home'),
    path("about/", views.about, name='dashboard-about'),
    path("predict/", views.predictmodel, name="dashboard-predict"),
    path("database/", views.prediction, name='dashboard-prediction'),
    path("main-view/", views.consumption, name='dashboard-consumption'),
    path("cintactus/", views.cintactus, name='cintactus')
]