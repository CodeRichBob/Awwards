from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.update_profile,name='profileUpdate'),
]