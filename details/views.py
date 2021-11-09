from django.shortcuts import render
# Create your views here.
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import(
    authenticate,
    get_user_model,
)
from django.contrib.auth import logout



def login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        auth_login(request,user)
        return HttpResponseRedirect("/")
    return render(request,'details/login.html',{"form":form})

    

@login_required(login_url='login')
def show(request):
    allYears  =  Year.objects.all()
    return render(request,'details/index.html',{
        "allyear":allYears,
    })


@login_required(login_url='login')
def showStudent(request,pk):
    allStudent = Info.objects.filter(year=pk)
    return render(request,'details/studentList.html',{
        "year":pk,
        "info":allStudent
    })

@login_required(login_url='login')
def addNewYear(request):    
    if request.method == 'POST':
        form = AddYear(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    else:
        form = AddYear()

    return render(request, 'details/addyear.html',{
        "form":form,
    })


@login_required(login_url='login')
def addNewStudent(request):
    if request.method == 'POST':
        form = AddStudent(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AddStudent()

    return render(request, 'details/addnewstudent.html',{
        "form":form,
    })

@login_required(login_url='login')
def editStudentDetails(request,pk,id):
    info = Info.objects.get(id=id)
    form = AddStudent(instance=info)

    if request.method == 'POST':
        print("yes")
        form = AddStudent(request.POST,instance=info)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/')
    else:
        form = AddStudent(instance=info)

    return render(request, 'details/editstudent.html',{
        "form":form,
    })


@login_required(login_url='login')
def deleteStudentDetails(request,pk,id):
    info = Info.objects.get(id=id)
    if request.method == 'POST':
        info.delete()
        return HttpResponseRedirect('/')
    return render(request, 'details/deletestudent.html',{
        "info":info,
    })



def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')