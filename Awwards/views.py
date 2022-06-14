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


@login_required(login_url='/accounts/login/')
def post_project(request): 
  '''Function handling post project'''
  if request.method == 'POST': 
    form = ProjectAddForm(request.POST,request.FILES)
    if form.is_valid(): 
      project=form.save(commit=False)
      project.project_owner = request.user 
      project.save()
      messages.success(request,'Your project has been successfully posted!')
      return redirect('home')
  else: 
    form = ProjectAddForm()

  return render(request,'projects/post_project.html',{"form":form})

def search_project(request): 
  '''Function handling search project'''
  if 'project' in request.GET and request.GET['project']: 
    search_term = request.GET.get('project')
    found_project = Projects.objects.filter(name=search_term).first()

  return render(request,'search_results.html',{"found_project":found_project})


@login_required(login_url='/accounts/login/')
def rate_project(request,project_id): 
  '''Function for rating a project'''
  project = Projects.objects.get(id=project_id)
  user = request.user 
  
  if request.method == 'POST': 
    form = ProjectRatingForm(request.POST)
    if form.is_valid(): 
      rate = form.save(commit=False)
      rate.user = user
      rate.project = project
      rate.save()
      return redirect('home')
  else: 
    form = ProjectRatingForm()
  return render(request,'projects/project_rating.html',{"project":project,"form":form})


