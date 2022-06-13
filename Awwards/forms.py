from django import forms
from .models import Profile,Projects,Ratings,RATE_CHOICES
from django.contrib.auth.models import User

# Profile form
class ProfileUpdateForm(forms.ModelForm): 
  class Meta: 
    model = Profile
    fields = ['bio','country','phone_number','picture']

# user update form
class UserUpdateForm(forms.ModelForm): 
  class Meta: 
    model = User
    fields = ['username','email']