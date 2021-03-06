from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    #Create relationship without enheritance
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Add any aditional attributes
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
