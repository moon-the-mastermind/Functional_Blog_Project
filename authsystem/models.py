from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from post_management.models import Post
from django.conf import settings

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    photo = models.ImageField(blank=True, null=True, upload_to="media/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        Group,  
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )

    user_permissions = models.ManyToManyField(
        Permission, 
        related_name="customuser_set_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    #social links
    facebook_link = models.URLField(null=True, blank=True)
    insta_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    
    def __str__(self):
        return self.user.username



    
