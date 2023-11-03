from django.db import models

class UserData(models.Model):
    photo = models.ImageField(upload_to='images/', default='No images')
    name = models.CharField(max_length=500, unique=True)
    
    
class CustomManager(models.Manager):
    pass

class AboutData(models.Model):
    fname = models.CharField(max_length=500, unique=True) 
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    objective = models.CharField(max_length=1000)
    linkin = models.CharField(max_length=500)
    github = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
    facebook = models.CharField(max_length=500)
    
class ExperienceData(models.Model):
    position = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    sdate = models.DateField(null=True, blank=True)
    edate = models.DateField(null=True, blank=True)
    
class EducationData(models.Model):
    university = models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    cgpa = models.CharField(max_length=500)
    pyear = models.DateField(null=True, blank=True)
    

class SkillsData(models.Model):
    language = models.CharField(max_length=500)
    licon = models.ImageField(upload_to='images/', default='No images')
    licon1 = models.ImageField(upload_to='images/', default='No images')
    licon2 = models.ImageField(upload_to='images/', default='No images')
    licon3 = models.ImageField(upload_to='images/', default='No images')
    licon4 = models.ImageField(upload_to='images/', default='No images')
    licon5 = models.ImageField(upload_to='images/', default='No images')
    licon6 = models.ImageField(upload_to='images/', default='No images')
    licon7 = models.ImageField(upload_to='images/', default='No images')
    licon8 = models.ImageField(upload_to='images/', default='No images')
    licon9 = models.ImageField(upload_to='images/', default='No images')
    licon10 = models.ImageField(upload_to='images/', default='No images')
    licon11 = models.ImageField(upload_to='images/', default='No images')
    workflow = models.CharField(max_length=500)
    wfone = models.CharField(max_length=500)
    wftwo = models.CharField(max_length=500)
    wfthree = models.CharField(max_length=500)
    wffour = models.CharField(max_length=500)
    wffive = models.CharField(max_length=500)
    
    
class InterestData(models.Model):
    interest = models.CharField(max_length=1000)
    othersinterest = models.CharField(max_length=1000)
    
class AwardsData(models.Model): 
    awards = models.CharField(max_length=500)
      