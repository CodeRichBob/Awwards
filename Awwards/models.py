from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
# creating projects model
class Projects(models.Model):
    project_owner = models.ForeignKey(User, on_delete = CASCADE)
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length=400)
    main_technology_used= models.CharField(max_length=30, null=True)
    screenshot=CloudinaryField('screenshot')
    live_link= models.URLField(max_length=100)
    date_added= models.DateField(auto_now_add=True)

    # saving a project
    def save_project(self):
        self.save()

    def __str__(self):
        return self.name

# creating profile model
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=CASCADE)
    bio = models.TextField(max_length = 400)
    country = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    picture = CloudinaryField('profile')

    def save_profile(self):
        '''Function to save a profile object'''
        self.save()
