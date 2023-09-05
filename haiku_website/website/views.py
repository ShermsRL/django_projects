from django.shortcuts import render
from django.http import HttpResponse

haiku_data = [
    {
        'author': 'Sherman Tay',
        'title': 'Haiku of the day',
        'haiku1': 'abcde',
        'haiku2': 'fghijkl',
        'haiku3': 'mnopq',
        'date_posted': 'September 4, 2023'
    },
    {
        'author': 'Sherman Tay',
        'title': 'Haiku of the day',
        'haiku1': 'abcde',
        'haiku2': 'fghijkl',
        'haiku3': 'mnopq',
        'date_posted': 'September 4, 2023'
    },
]

# Create your views here.
def home(request):
    context = {
        'author': 'Sherman Tay',
        'title': 'Haiku of the day',
        'haiku1': 'abcde',
        'haiku2': 'fghijkl',
        'haiku3': 'mnopq',
        'date_posted': 'September 4, 2023'
    }

    return render(request, 'website/home.html', context)


def about(request):
    return render(request, 'website/about.html', {'title': 'About'})


def haikus(request):
    context = {
        'haikus': haiku_data
    }

    return render(request, 'website/haikus.html', context)