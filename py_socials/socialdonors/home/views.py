from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'home/index.html', context)