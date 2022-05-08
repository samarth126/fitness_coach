from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    username=None
    first_name=models.CharField(null=True, max_length=11, default="x")
    last_name=models.CharField(null=True, max_length=11, default="x")
    email=models.EmailField(unique=True, null=False)
    phone_no=models.CharField(max_length=11, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects=UserManager()
    REQUIRED_FIELDS=[]


class food(models.Model):
    food_user=models.ForeignKey(User, on_delete=models.RESTRICT)
    food_name=models.CharField(null=True, max_length=11)
    food_quant=models.CharField(null=True, max_length=11)
    calories=models.CharField(null=True, max_length=11)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.food_name)


class workout(models.Model):
    workout_user=models.ForeignKey(User, on_delete=models.RESTRICT)
    workout_name=models.CharField(null=True, max_length=11)
    goal=models.IntegerField(default=5,blank = True)
    achived=models.IntegerField(default=5,blank = True)
    msic_type=models.CharField(null=True, max_length=11, default='rock')
    reps=models.IntegerField(default=5,blank = True)
    tot_cal=models.IntegerField(default=10,blank = True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.workout_name)

class daily_info(models.Model):
    daily_user=models.ForeignKey(User, on_delete=models.RESTRICT)
    spo2=models.IntegerField(default=5,blank = True)
    heart_rate=models.IntegerField(default=5,blank = True)
    sleep=models.IntegerField(default=5,blank = True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.daily_user)

class profile(models.Model):
    pro_user=models.OneToOneField(User, on_delete=models.RESTRICT)
    height=models.CharField(null=True, max_length=11)
    weight=models.CharField(null=True, max_length=11)
    bmi=models.CharField(null=True, max_length=11)
    body_type=models.CharField(null=True, max_length=11)
    def __str__(self):
        return str(self.pro_user)


class Notifications(models.Model):
    notification_user=models.ForeignKey(User, on_delete=models.RESTRICT)
    time=models.DateTimeField(auto_now_add=True)
    message=models.TextField(blank=True)

    def __str__(self):
        return str(self.notification_user)

class contact(models.Model):
    name=models.CharField(null=True, max_length=11)
    email=models.CharField(null=True, max_length=11)
    message=models.CharField(null=True, max_length=11)

    def __str__(self):
        return str(self.name)

