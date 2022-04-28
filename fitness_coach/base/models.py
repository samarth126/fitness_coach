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
    food_quant=models.IntegerField(max_length=5, default=100)
    calories=models.CharField(null=True, max_length=11)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.food_name)


class workout(models.Model):
    workout_user=models.ForeignKey(User, on_delete=models.RESTRICT)
    workout_name=models.CharField(null=True, max_length=11)
    reps=models.IntegerField(max_length=5, default=100)
    tot_cal=models.IntegerField(max_length=5, default=100)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.workout_name)

class profile(models.Model):
    pro_user=models.OneToOneField(User, on_delete=models.RESTRICT)
    height=models.CharField(null=True, max_length=11)
    weight=models.CharField(null=True, max_length=11)
    bmi=models.CharField(null=True, max_length=11)
    body_type=models.CharField(null=True, max_length=11)
    def __str__(self):
        return str(self.workout_name)

