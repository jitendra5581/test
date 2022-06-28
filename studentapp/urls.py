from .views import *
from django.urls import path

urlpatterns = [
    path('home/', home_view),
    path('login/', login_view),
    path('about/', about_view),
    ]