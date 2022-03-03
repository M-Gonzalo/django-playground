from django.urls import path
from . import views

urlpatterns = [
    path('index-old', views.index_old, name='index'),
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('counter', views.counter, name='counter'),
]
