from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .forms import Registration
from django.contrib import messages

def home(request):
    context = {

    }
    return  render(request,'index.html',context)

def Sign(request):

    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'রেজিস্ট্রেশন সম্পন্ন হয়েছে')
            return redirect('Home')
    else:
      form = Registration()
    context ={
        'form':form
    }
    return render(request, 'profile/sign.html', context)


def Login(request):
   if request.method == 'POST':
      form = AuthenticationForm(request=request, data=request.POST)
      if form.is_valid():
         username = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password')
         user = authenticate(username=username, password=password)
         if user is not None:
            login(request, user)
            messages.success(request, 'লগইন সফল হয়েছে')
            return redirect('Home')
         else:
            messages.error(request, 'ভুল পাসওয়ার্ড ও ই-মেইল ব্যবহার করেছেন')
      else:
         messages.error(request, 'ভুল পাসওয়ার্ড ও ই-মেইল ব্যবহার করেছেন')
   else:
      form = AuthenticationForm()
   return render(request, 'profile/login.html', {'form': form})


def Logout(request):
   logout(request)
   messages.success(request, 'লগআউট সম্পন্ন হয়েছে')
   return redirect('Home')
