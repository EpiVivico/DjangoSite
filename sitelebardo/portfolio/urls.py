from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
