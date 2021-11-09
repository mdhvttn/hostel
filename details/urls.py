
from django.contrib import admin
from django.urls import path,include
from . import views




urlpatterns = [
    path('login',views.login,name='login'),
    path('',views.show,name='home'),
    path('addyear',views.addNewYear,name='newyear'),
    path('<int:pk>/',views.showStudent,name='studentlist'),
    path('addnewstudent/',views.addNewStudent,name='newstudent'),
    path('<int:pk>/<int:id>/editstudent',views.editStudentDetails,name='editstudent'),
    path('<int:pk>/<int:id>/deletestudent',views.deleteStudentDetails,name='deletestudent'),
    path('logout',views.logoutView,name='logout'),
]   







