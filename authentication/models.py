from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'authentication'  # Specify the app_label
class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    college_attended = models.CharField(max_length=100)
    grades_percentage = models.FloatField()
    parents_income = models.FloatField()
    first_choice_faculty = models.CharField(max_length=100)
    second_choice_faculty = models.CharField(max_length=100)
    third_choice_faculty = models.CharField(max_length=100)
    achievements = models.TextField()

    def __str__(self):
        return self.user.username