from . import views
from django.urls import path
from django.views.generic import RedirectView

urlpatterns =[
    path('', views.home, name='home'),
]