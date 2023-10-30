from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Import the datetime module
from datetime import datetime  
from user.models import UserData,AboutData,ExperienceData,EducationData,SkillsData,InterestData,AwardsData
# Create your views here.



def portfolio_index(request):
    profile_data = UserData.objects.all()
    about_data = AboutData.objects.all()
    experience_data = ExperienceData.objects.all()
    education_data = EducationData.objects.all()
    skills_data = SkillsData.objects.all()
    interest_data = InterestData.objects.all()
    awards_data = AwardsData.objects.all()
    data = {"user_info": profile_data, 
            "about_info":about_data,
            "experience_info":experience_data,
            "education_info":education_data,
            "skills_info":skills_data,
            "interest_info":interest_data,
            "awards_info":awards_data,
            }
    return render(request, 'index.html', data)

def output_profile(request):
    profile_data = UserData.objects.all()
    if(len(profile_data)==0):
        status = False
    else:
        status = True
    data = {"user_data": profile_data, 'status': status}
    return render(request,'index.html', data)

def output_about(request):
    
    about_data = AboutData.objects.all()
    if(len(about_data)==0):
        status = False
    else:
        status = True
    data = {"about_info": about_data, 'status': status}
    return render(request,'index.html', data)
        
def output_experience(request):
    
    experience_data = ExperienceData.objects.all()
    if(len(experience_data)==0):
        status = False
    else:
        status = True
    data = {"experience_info": experience_data, 'status': status}
    return render(request,'index.html', data)   


def output_education(request):
    
    education_data = EducationData.objects.all()
    if(len(education_data)==0):
        status = False
    else:
        status = True
    data = {"education_info": education_data, 'status': status}
    return render(request,'index.html', data)   


def output_skills(request):
    
    skills_data = SkillsData.objects.all()
    if(len(skills_data)==0):
        status = False
    else:
        status = True
    data = {"skills_info": skills_data, 'status': status}
    return render(request,'index.html', data) 


def output_interest(request):
    
    interest_data = InterestData.objects.all()
    if(len(interest_data)==0):
        status = False
    else:
        status = True
    data = {"interest_info": interest_data, 'status': status}
    return render(request,'index.html', data) 


def output_awards(request):
    
    awards_data = AwardsData.objects.all()
    if(len(awards_data)==0):
        status = False
    else:
        status = True
    data = {"awards_info": awards_data, 'status': status}
    return render(request,'index.html', data)      

