from django.shortcuts import render
from .forms import UserLogin

def login(request):
    form = UserLogin()

    if request.method == 'POST':
        pass
    else: 
        form = UserLogin()
        
    return render(request, "user_login.html", {'form': form})