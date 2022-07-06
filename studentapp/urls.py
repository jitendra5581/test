from .views import *
from django.urls import path

urlpatterns = [
    path('home/', home_view),
    path('login/', login_view),
    path('about/', about_view),
    path('delete/', delete_view),
    path('details/', details_view),
    path('edit/', edit_view),
    ]