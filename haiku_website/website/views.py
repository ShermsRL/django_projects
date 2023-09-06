from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    context = {
        'haikus': Post.objects.get(id=1)
    }

    return render(request, 'website/home.html', context)


def about(request):
    return render(request, 'website/about.html', {'title': 'About'})


def haikus(request):
    context = {
        'haikus': Post.objects.all()
    }

    return render(request, 'website/haikus.html', context)