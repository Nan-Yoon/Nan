from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('second/', views.second, name='second'),
    path('student/', views.student, name='student'),
    path('add/', views.add, name="add"),
    path('add/addrecord/', views.addrecord, name="addrecord"),
    path('showstudent/', views.showstudent, name='showstudent'),
]