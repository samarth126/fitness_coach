from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.http.response import JsonResponse
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import User, food
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
        if request.method == 'POST':
            food_name = request.POST.get('food_name')
            food_quant = request.POST.get('food_quant') 
            calories = request.POST.get('calories') 
            us= request.user
            fd = food(food_user=us,food_name=food_name,food_quant=food_quant,calories=calories )
            fd.save()
    else:
        return redirect('loginr')
    return render(request , 'food.html',{'ssu':ssu, 'phone':phone})



def result(request):
    return render(request , 'results.html')



def profile(request):
    if request.user.is_authenticated:
        ssu=request.user
        phone=request.user.phone_no

    else:
        ssu="you aare not loged in pls log in"
        phone=9999999

    return render(request, 'profile.html',{'ssu':ssu,'phone':phone})



def cam_but(request):
    if request.method == 'POST':
        s=ml.camm()
        print(s)
    return render(request, 'cool.html',{'som':s})



def cool(request):
    s=ml.hell(request)
    print(s)
    return render(request, 'cool.html',{})


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

