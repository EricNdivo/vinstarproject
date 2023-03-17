from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return HttpResponse("Coming Soon...")

def signup(request):
    print(request.user)
    if request.method == 'POST':
        username = username.POST.get('username')
        email = request.POST.get('lastname')
        password = request.POST.get('password')
        password_conf = request.POST.get('password_conf')
        
        try:
            if User.objects.filter(username=username):
                messages.error(request, 'Username already in use')
        except:
            messages.error(request, 'Service Failed')
            
        if User.objects.filter(email=email):
            messages.error(request, 'Invalid Email Address')
            
        if len(username)>10:
            messages.error(request, '#')
            
        try:
            user = User.objects.create_user(username=username, email=email)
            user.save()
        except:
            messages.error(request,'User not created')
        
    return render(request, 'signup.html')



def login(request):
    print(request.user)
    pass        

            