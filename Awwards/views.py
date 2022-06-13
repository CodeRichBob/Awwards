from django.shortcuts import render

# Create your views here.
def home(request): 
  '''Function rendering the home page'''
  
  projects = Projects.objects.all() #obtaining all posted projects

  return render(request,'index.html',{"projects":projects})
