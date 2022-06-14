from django.shortcuts import render

# Create your views here.
def home(request): 
  '''Function rendering the home page'''
  
  projects = Projects.objects.all() #obtaining all posted projects

  return render(request,'index.html',{"projects":projects})

def profile(request): 
  '''Function rendering a logged in user's profile page'''
  profile = Profile.objects.filter(user=request.user).first()
  user_projects = Projects.objects.filter(project_owner=request.user).all()
  return render(request,'registration/profile.html',{"profile":profile,"user_projects":user_projects})

