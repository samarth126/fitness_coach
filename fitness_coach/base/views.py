from cProfile import Profile
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.http.response import JsonResponse
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import RForm
from django.contrib import messages
from Machine_L import ml
# Create your views here.


def home(request):
    return render(request , 'index.html')



def food1(request):
    if request.user.is_authenticated:
        ssu=request.user
        phone=request.user.phone_no
        food1 = food.objects.filter(food_user=ssu).order_by('-id')
        if request.method == 'POST':
            food_name = request.POST.get('food_name')
            food_quant = request.POST.get('food_quant') 
            calories = request.POST.get('calories') 
            us= request.user
            fd = food(food_user=us,food_name=food_name,food_quant=food_quant,calories=calories )
            fd.save()
    else:
        return redirect('loginr')
    return render(request , 'food.html',{'ssu':ssu, 'phone':phone, 'food1':food1})



def health(request):
    if request.user.is_authenticated:
        user=request.user
        healthy = daily_info.objects.filter(daily_user=user).order_by('-id')
        if request.method == 'POST':
            spo2 = request.POST.get('spo2')
            heart_rate = request.POST.get('heart_rate')
            sleep = request.POST.get('sleep')
            healt=daily_info(daily_user=user,spo2=spo2, heart_rate=heart_rate, sleep=sleep)
            healt.save()
    else:
        return redirect('loginr')
    return render(request , 'health.html',{'user':user,'healthy':healthy})



def result(request):
    if request.user.is_authenticated:
        user=request.user
        food1 = food.objects.filter(food_user=user).order_by('-id')
        healthy = daily_info.objects.filter(daily_user=user).order_by('-id')
        work1 = workout.objects.filter(workout_user=user).order_by('-id')
    else:
        return redirect('loginr')
    return render(request , 'results.html',{'user':user,'food1':food1,'healthy':healthy, 'work1':work1})



def noti(request):
    if request.user.is_authenticated:
        ssu=request.user
        notify=Notifications.objects.filter(notification_user=ssu)

    else:
        return redirect('loginr')

    return render(request, 'noti.html',{'ssu':ssu, 'notify':notify})


def contactt(request):
    if request.method == 'POST':
            cf_name = request.POST.get('cf_name')
            cf_email = request.POST.get('cf_email')
            cf_message = request.POST.get('cf_message')
            conc=daily_info(name=cf_name, email=cf_email, message=cf_message)
            conc.save()

    return render(request, 'index.html',{})



def profilee(request):
    if request.user.is_authenticated:
        ssu=request.user
        prof, created = profile.objects.get_or_create(pro_user=ssu)

    else:
        return redirect('loginr')

    return render(request, 'profile.html',{'ssu':ssu, 'prof':prof})



def cam_but(request):
    if request.user.is_authenticated:
        user=request.user
        if request.method == 'POST':
            s=ml.camm()
        print(s)
    else:
        return redirect('loginr')
    return render(request, 'cool.html',{'som':s})



def cool(request):
    reps=0
    achived=5
    if request.user.is_authenticated:
        user=request.user
        work1 = workout.objects.filter(workout_user=user).order_by('-id')
        if request.method == 'POST':
            reps=ml.camm()
            workout_name = request.POST.get('workout_name')
            goal = request.POST.get('goal') 
            msic_type = request.POST.get('msic_type') 
            tot_cal = request.POST.get('tot_cal') 
            wrk = workout(workout_user=user,workout_name=workout_name,goal=goal, achived =achived ,msic_type=msic_type,reps=reps,tot_cal=tot_cal )
            wrk.save()
    else:
        return redirect('loginr')
    
    print(reps)
    return render(request, 'cool.html',{'s':reps, 'user':user, 'work1':work1})


def register(request):
   
    form = RForm()
    if request.method == 'POST':
        form = RForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginr')
        else:
            return HttpResponse("not working")
               
        
    context={'form':form}
    return render(request, 'loginr.html',context)







def loginr(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        emailw = request.POST.get('email')
        passs = request.POST.get('password') 
        try:
            user = User.objects.get(email=emailw)
            
        except:
            messages.error(request, '{} does not exist'.format(emailw))

        user=authenticate(request, email=emailw, password=passs)   
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username password does not exist')

    
   
    # return render(request,'loginr.html', context)
    
    return render(request, 'login.html')





def logoutUser(request):
    logout(request)
    return redirect('home')

