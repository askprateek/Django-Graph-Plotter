from django.conf.urls import url
from django.contrib import admin
from bokeh_app import views

urlpatterns = [
    url(r'^$', views.index ),
]
