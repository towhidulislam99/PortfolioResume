from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Import the datetime module
from user.models import UserData,AboutData,ExperienceData,EducationData,SkillsData,InterestData,AwardsData


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


