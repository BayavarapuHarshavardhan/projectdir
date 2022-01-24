from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact')
]
admin.site.site_header = "Harshavardhan's Admin"
admin.site.site_title = "Harsha's Admin Portal"
admin.site.index_title = "Welcome to Lunatic Portal"