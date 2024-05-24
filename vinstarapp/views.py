from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Property, Agent 
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return HttpResponse("Coming Soon...")
           
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')

def seemore(request):
    print(request.user)
    return render(request, 'main.html')

def services(request):
    print(request.user)   
    return render(request, 'services.html')

@login_required
def user_profile(request):
    print(request.user)

    user = request.user

    username = user.username
    email = user.email

    context = {
        'username': username,
        'email': email,
    }
    return render(request, 'user_info.html', context)

def user_management(request):
    print(request.user)

    return render(request, 'user_management.html')

def property_search(request):
    print(request.user)

    keyword = request.GET.get('keyword', '')
    property_type = request.GET.get('property_type', '')
    location = request.GET.get('location', '')

    properties = Property.objects.all()

    if keyword:
        properties = properties.filter(name__icontains=keyword)
    if property_type:
        properties = properties.filter(property_type=property_type)
    if location:
        properties = properties.filter(location=location)


    agents = Agent.objects.all()

    context ={
        'properties': properties,
        'agents': agents,
    }
    return render(request, 'main.html', context)