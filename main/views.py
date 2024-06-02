from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Orphan

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('manage_orphans')
        else:
            # Add error message for invalid credentials
            pass
    return render(request, 'login.html')

@login_required
def manage_orphans(request):
    orphans = Orphan.objects.all()
    return render(request, 'manage_orphans.html', {'orphans': orphans})
