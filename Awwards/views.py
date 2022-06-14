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

@login_required(login_url='/accounts/login/')
def update_profile(request): 
  '''Function for user profile update'''
  profile = Profile.objects.filter(user=request.user).first()
  if request.method == 'POST': 
    u_form = UserUpdateForm(request.POST,instance=request.user)
    p_form = ProfileUpdateForm(request.POST,request.FILES,instance=profile)
    if u_form.is_valid() and p_form.is_valid(): 
      u_form.save()
      user_profile=p_form.save(commit=False)
      user_profile.user = request.user 
      user_profile.save()
      messages.success(request,'Your account has been updated!')
      return redirect('profile')
  else: 
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=profile)
  
  context = {
    'u_form': u_form,
    'p_form': p_form
  }
  return render(request,'registration/update_profile.html',context)

