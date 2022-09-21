from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Mkoa(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Wilaya(models.Model):
    name = models.CharField(max_length=30)
    mkoa_id = models.ForeignKey(Mkoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(AbstractUser):
    choice = (("farmer", "farmer"), ("admin", "admin"),)
    phone = models.CharField(max_length=10)
    type = models.CharField(max_length=20, choices=choice, default='farmer')
    created_at = models.DateField(auto_now_add=True, null=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class AdminProfile(models.Model):
    choice = (("soil", "soil"), ("weather", "weather"), ("agriculture", "agriculture"),)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    institute_logo = models.ImageField(upload_to="admin_profile/", null=True, blank=True)
    institute = models.CharField(max_length=100, null=False)
    wilaya_id = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=choice, null=False)

    def __str__(self):
        return self.institute
