from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Product
# Create your views here.

#User registration view
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        if password == confirm_password :
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, 'Registeration Successful. Please login.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'store/register.html')


#User login view
def user_login(request):
    if request.method =='POST':
        username == request.POST['username']
        password == request.POST['password']
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request,user)
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid username or Password.')
    return render(request, 'store/login.html')

#user logout view
def user_logout(request):
    logout(request)
    return redirect('login')
    
    

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product' : product})
