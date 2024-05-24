from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('signout', views.signout, name='signout'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('seemore', views.seemore, name='seemore'),
    path('services', views.services, name='services'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('user_management',views.user_management,name='user_management'),
    path('search', views.property_search, name='property_search')
]