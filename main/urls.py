from django.urls import path
from . import views

url_patterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('project/<int:id>',views.project,name='project'),
]