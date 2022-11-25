from django.shortcuts import render, redirect

# Create your views here.
def login_request(request):
    
    return render(request, 'login.html')