from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'pictures/')
    bio=models.TextField()
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    user_name=models.CharField(max_length=20,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()

    # update profile
    def update_profile(self, name):
        self.name = name
        self.save()

     # delete profile from database
    def delete_profile(self):
        self.delete()
        
        