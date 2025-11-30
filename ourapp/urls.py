from django.urls import path
from . import views

urlpatterns = [
    # Home Page (name='home' ang ginagamit sa links)
    path('', views.home_view, name='home'), 
    
    # New Paths
    path('achievements/', views.achievements_view, name='achievements'),
    path('neville/', views.neville_view, name='neville_profile'),
    path('emriz/', views.emriz_view, name='emriz_profile'),
]