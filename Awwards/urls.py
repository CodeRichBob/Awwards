from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.update_profile,name='profileUpdate'),
    path('post_project/',views.post_project,name='post_project'),
    path('search/project/',views.search_project,name='search_project'),
]