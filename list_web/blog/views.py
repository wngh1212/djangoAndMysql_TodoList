from .models import Posts
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login


def index(request):
  Post = Posts.objects.all()
  return render(request, "index.html",{"Post":Post})


# @require_POST
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        # Redirect to a success page or home page
        return redirect('index')  # Change 'index' to your actual home page name
    else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    

    return render(request, 'login.html')

