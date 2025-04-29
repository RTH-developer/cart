from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import customer

# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            # create user account
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            # create customer account
            Customer = customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            # return redirect('home')
            success_message="successfully registered"
            messages.success(request,success_message)

        except Exception as e:
            # You should handle the exception here
            error_message="Duplicate username or invalid input"
            messages.error(request,error_message)
            # You might want to add a message to the user
            # or render the template with an error message
    if request.POST and 'login' in request.POST:
        context['register']=False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user credentials')    
        

    return render(request, 'account.html',context)