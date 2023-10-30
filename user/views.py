from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse,HttpResponseBadRequest
import os
from django.http import Http404
# Import the datetime module
from datetime import datetime  
# Create your views here.
from .models import UserData,AboutData,ExperienceData,EducationData,SkillsData,InterestData,AwardsData
from portfolio.views import portfolio_index


def user_index(request):
    return render(request, 'admin.html')

def user_panel(request):
    return render(request, 'user.html')

def user_data(request):
    return render(request, 'navbarinput.html')

# Navbar Form  Data Insert.
def insert_data(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        name = request.POST.get('name')
    
        # Validate that 'name' is not empty
        if name:
            # Create User Data Object.
            user_obj = UserData()
            
            user_obj.photo = photo
            user_obj.name = name
            user_obj.save()
            messages.success(request,"Data has been Successfully Submitted.")
            return redirect('user_user')
        else:
            return HttpResponse('Empty Fields not be acceptted')
    else:
        return render(request, 'user.html')
    
def output_data(request):
    profile_data = UserData.objects.all()
    data = {"user_data": profile_data}
    return render(request,'index.html', data)

def edit_data(request, id):
    profile_data = UserData.objects.get(id=id)
    data = {"user_data": profile_data}
    return render(request,'updatenavbar.html', data)
    
def update_data(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    
    user_obj = get_object_or_404(UserData, id=id)
    
    if 'photo' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if user_obj.photo:
            os.remove(user_obj.photo.path)
        user_obj.photo = request.FILES['photo']
    user_obj.name = name
    user_obj.save() 
    return redirect('portfolio_index')

def user_about(request):
    return render(request, 'about.html')

# About Form  Data Insert.
def insert_about(request):
   if request.method == 'POST':
       fname = request.POST.get('fname')
       address = request.POST.get('address')
       email = request.POST.get('email')
       objective = request.POST.get('objective')
       linkin = request.POST.get('linkin')
       github = request.POST.get('github')
       twitter = request.POST.get('twitter')
       facebook = request.POST.get('facebook')
       
       if fname:
        # Create User Data Object.
          about_obj = AboutData()
          about_obj.fname = fname
          about_obj.address = address
          about_obj.email = email
          about_obj.objective = objective
          about_obj.linkin = linkin
          about_obj.github = github
          about_obj.twitter = twitter
          about_obj.facebook = facebook
          about_obj.save()
          messages.success(request,"Data has been Successfully Submitted.")
          return redirect('user_user') 
       else:
             return HttpResponse('Empty Fields not be acceptted')
   else:
        return render(request, 'user.html')
       
def edit_about(request, id):
    profile_data = AboutData.objects.get(id=id)
    data = {"about_data": profile_data}
    return render(request, 'updateabout.html', data)

def update_about(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if not id:
            fname = request.POST.get('fname')
            address = request.POST.get('address')
            email = request.POST.get('email')
            objective = request.POST.get('objective')
            linkin = request.POST.get('linkin')
            github = request.POST.get('github')
            twitter = request.POST.get('twitter')
            facebook = request.POST.get('facebook')
            # Handle the case when 'id' is missing in the POST request
            raise Http404("ID parameter is missing in the request.")

        about_obj = get_object_or_404(AboutData, id=id)
        about_obj.fname = fname
        about_obj.address = address
        about_obj.email = email
        about_obj.objective = objective
        about_obj.linkin = linkin
        about_obj.github = github
        about_obj.twitter = twitter
        about_obj.facebook = facebook
        about_obj.save()
        return redirect('portfolio_index')


# def update_about(request):
#         id = request.POST.get('id')
#         fname = request.POST.get('fname')
#         address = request.POST.get('address')
#         email = request.POST.get('email')
#         objective = request.POST.get('objective')
#         linkin = request.POST.get('linkin')
#         github = request.POST.get('github')
#         twitter = request.POST.get('twitter')
#         facebook = request.POST.get('facebook')
        
#         about_obj = get_object_or_404(AboutData, id=id)
#         about_obj.fname = fname
#         about_obj.address = address
#         about_obj.email = email
#         about_obj.objective = objective
#         about_obj.linkin = linkin
#         about_obj.github = github
#         about_obj.twitter = twitter
#         about_obj.facebook = facebook
#         about_obj.save()
#         return redirect('portfolio_index')

def user_experience(request):
    return render(request, 'experience.html')

# Experience Form  Data Insert.
def insert_experience(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        company = request.POST.get('company')
        description = request.POST.get('description')
        sdate = request.POST.get('sdate')  
        edate = request.POST.get('edate') 

        if position:
            experience_obj = ExperienceData()
            experience_obj.position = position
            experience_obj.company = company
            experience_obj.description = description

            if sdate and edate:
                experience_obj.sdate = datetime.strptime(sdate, '%Y-%m-%d').date()
                experience_obj.edate = datetime.strptime(edate, '%Y-%m-%d').date()
                experience_obj.save()
                messages.success(request, "Data has been successfully submitted.")
                return redirect('user_user')
            else:
                messages.error(request, "Failed to submit data: Invalid date format or missing date.")
        else:
            messages.error(request, "Failed to submit data: Position is required.")
    return render(request, 'user.html')

def user_education(request):
    return render(request, 'education.html')

def insert_education(request):
    if request.method == 'POST':
        university = request.POST.get('university')
        degree = request.POST.get('degree')
        subject = request.POST.get('subject')
        cgpa = request.POST.get('cgpa')
        pyear = request.POST.get('pyear')
        
        if university:
            
            education_obj = EducationData()
            education_obj.university = university
            education_obj.degree = degree
            education_obj.subject = subject
            education_obj.cgpa = cgpa
            if pyear:
                education_obj.pyear = datetime.strptime(pyear,'%Y-%m-%d').date() 
                education_obj.save()
                messages.success(request, "Data has been successfully submitted.")
                return redirect('user_user')
            else:
                messages.error(request, "Failed to submit data: Invalid date format or missing date.")
        else:
            messages.error(request, "Failed to submit data: Position is required.")
    return render(request, 'user.html')


def user_skills(request):
    return render(request, 'skills.html')

def insert_skills(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        workflow = request.POST.get('workflow')
        wfone = request.POST.get('wfone')
        wftwo = request.POST.get('wftwo')
        wfthree = request.POST.get('wfthree')
        wffour = request.POST.get('wffour')
        wffive = request.POST.get('wffive')
        
        if language:
            
            skills_obj = SkillsData()
            skills_obj.language = language
            skills_obj.workflow = workflow
            skills_obj.wfone = wfone
            skills_obj.wftwo = wftwo
            skills_obj.wfthree = wfthree
            skills_obj.wffour = wffour
            skills_obj.wffive = wffive
            skills_obj.save()
        else:
            messages.error(request, "Failed to submit data: Invalid Data")
    else:
        messages.error(request, "Failed to submit data: Position is required.")
    return render(request, 'user.html')
        

def user_interest(request):
    return render(request, 'interest.html')

def insert_interest(request):
   if request.method == 'POST':
       interest = request.POST.get('interest')
       othersinterest = request.POST.get('othersinterest')
       if interest:
           
           interest_obj = InterestData()
           interest_obj.interest = interest
           interest_obj.othersinterest = othersinterest
           interest_obj.save()
       else:
           messages.error(request, "Failed to submit data: Invalid Data")
   else:
        messages.error(request, "Failed to submit data: Position is required.")
   return render(request, 'user.html')

def user_awards(request):
    return render(request, 'awards.html')

def insert_awards(request):
    if request.method == 'POST':
        awards = request.POST.get('awards')
        
        if awards:
            
            awards_obj = AwardsData()
            awards_obj.awards = awards
            awards_obj.save()
        else:
           messages.error(request, "Failed to submit data: Invalid Data")
    else:
        messages.error(request, "Failed to submit data: Position is required.")
    return render(request, 'user.html')