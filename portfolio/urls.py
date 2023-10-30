"""
URL configuration for portfolioResume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views as v

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('index/', v.portfolio_index, name='portfolio_index'),
     
    #  path('Profile/', v.output_profile, name='output_profile'),
    #  path('about/', v.output_about, name='output_about'),
    #  path('experience/', v.output_experience, name='output_experience'),
    #  path('education/', v.output_education, name='output_education'),
    #  path('skills/', v.output_skills, name='output_skills'),
    #  path('interest/', v.output_interest, name='output_interest'),
    #  path('awards/', v.output_awards, name='output_awards'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
