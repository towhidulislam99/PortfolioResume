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
    path('', v.user_index, name='user_index'),
    path('user/', v.user_panel, name='user_user'),
    path('data/', v.user_data, name='user_data'),
    path('insertdata/', v.insert_data, name='insert_data'),
    path('editdata/<int:id>', v.edit_data, name='edit_data'),
    path('updatedata/', v.update_data, name='update_data'),
    path('deletedata/<int:id>', v.delete_data, name='delete_data'),
    path('about/', v.user_about, name='user_about'),
    path('insertabout/', v.insert_about, name='insert_about'),
    path('editabout/<int:id>', v.edit_about, name='edit_about'),
    path('updateabout/', v.update_about, name='update_about'),
    path('deleteabout/<int:id>', v.delete_about, name='delete_about'),
    path('experience/', v.user_experience, name='user_experience'),
    path('insertexperience/', v.insert_experience, name='insert_experience'),
    path('editexperience/<int:id>', v.edit_experience, name='edit_experience'),
    path('updateexperience/', v.update_experience, name='update_experience'),
    path('deleteexperience/<int:id>', v.delete_experience, name='delete_experience'),
    path('education/', v.user_education, name='user_education'),
    path('inserteducation/', v.insert_education, name='insert_education'),
    path('editeducation/<int:id>', v.edit_education, name='edit_education'),
    path('updateeducation/', v.update_education, name='update_education'),
    path('deleteeducation/<int:id>', v.delete_education, name='delete_education'),
    path('skills/', v.user_skills, name='user_skills'),
    path('insertskills/', v.insert_skills, name='insert_skills'),
    path('editskills/<int:id>', v.edit_skills, name='edit_skills'),
    path('updateskills/', v.update_skills, name='update_skills'),
    path('deleteskills/<int:id>', v.delete_skills, name='delete_skills'),
    path('interest/', v.user_interest, name='user_interest'),
    path('insertinterest/', v.insert_interest, name='insert_interest'),
    path('editinterest/<int:id>', v.edit_interest, name='edit_interest'),
    path('updateinterest/', v.update_interest, name='update_interest'),
    path('deleteinterest/<int:id>', v.delete_interest, name='delete_interest'),
    path('awards/', v.user_awards, name='user_awards'),
    path('insertawards/', v.insert_awards, name='insert_awards'),
    path('editawards/<int:id>', v.edit_awards, name='edit_awards'),
    path('updateawards/', v.update_awards, name='update_awards'),
    path('deleteawards/<int:id>', v.delete_awards, name='delete_awards'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
