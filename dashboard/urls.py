from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('linechart', views.linechart, name='linechart'),
    path('piechart', views.piechart, name='piechart'),
    path('table', views.table, name='table'),
]