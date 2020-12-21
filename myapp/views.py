from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from .forms import CompanyForm
from .models import CompanyDetail

# Create your views here.
# signup form create view functioin

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'acoount created successfully')
            fm.save() 
    else :        
        fm = SignupForm()
    return render(request,'myapp/signup.html',{'form':fm})

# create login view function

def loginpage(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request= request, data= request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                auth.login(request, user)    
                return HttpResponseRedirect('/insert/')
    else:
        fm = AuthenticationForm()
    return render(request,'myapp/login.html',{'form':fm})

# insert function

def insert(request):
    if request.method == 'POST':
        fm = CompanyForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm=CompanyForm()
    else:
        fm = CompanyForm()    
    return render(request,'myapp/insert.html',{'fm':fm})


# show function     

def show(request):
    CompanyDetails = CompanyDetail.objects.all() 
    return render(request,'myapp/show.html',{'CompanyDetails':CompanyDetails})    

def update_data(request, id):
    if request.method == 'POST':
        pi = CompanyDetail.objects.get(pk=id)
        fm = CompanyForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = CompanyDetail.objects.get(pk=id)
        fm = CompanyForm(request.POST, instance=pi)
    return render(request,'myapp/update.html',{'form':fm})


# this function will delete item
def delete_data(request, id):
        pi = CompanyDetail.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/insert/')    