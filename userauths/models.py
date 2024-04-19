from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=100, default="Firstname")
    last_name = models.CharField(max_length=100, default="Lastname")
    bio = models.CharField(max_length=100, blank=True, null=True)
    house_address = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="Mauritius")
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="image", null=True, blank=True)
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    bio = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, default=" ")
    house_address = models.CharField(max_length=500, default=" ")
    city = models.CharField(max_length=500, default=" ")
    country = models.CharField(max_length=500, null=True, blank=True, default="Mauritius")
    
    verified = models.BooleanField(default=False)
    
    
    
    def __str__(self):
            return self.user.first_name
    

def create_user_profile(sender, instance, created, **kwargs):
    if created: 
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(default="email@abc.com")
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    information = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f"{self.full_name}"