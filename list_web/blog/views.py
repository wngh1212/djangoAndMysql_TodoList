from django.shortcuts import render
from .models import Posts
def index(request):
  Post = Posts.objects.all()
  return render(request, "index.html",{"Post":Post})