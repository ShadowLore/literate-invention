from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name='home'),
        path('philosopher1', views.philosopher1, name='philosopher1'),
        path('philosopher2', views.philosopher2, name='philosopher2'),
        path('philosopher3', views.philosopher3, name='philosopher3'),
        path('philosopher4', views.philosopher4, name='philosopher4'),
        path('philosopher5', views.philosopher5, name='philosopher5'),
]
