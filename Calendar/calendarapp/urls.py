from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar-view'),
]
