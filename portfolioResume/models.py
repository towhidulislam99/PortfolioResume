from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for the user profile
    
    # Add other profile information here

    def __str__(self):
        return self.user.username
