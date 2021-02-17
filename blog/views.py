from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home (request):
    last_twenty = Post.objects.all().order_by('-id')[:10]
    return render(request, 'index.html', {'posts':last_twenty})

