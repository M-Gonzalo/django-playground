from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def index_old(request):
    context = {
        'name': 'Gonzalo',
        'background_image': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80',
        # Get a random background image from the unsplash API every time the page is loaded
        'random_background_image': 'https://source.unsplash.com/random?animals',
        # Calculate my age from my birthday (08-nov-1990), and add it to the context
        'age': (lambda: int(((datetime.datetime.now() - datetime.datetime(1990, 11, 8)).days) / 365.25))(),
        'portfolio_url': 'https://github.com/m-gonzalo'
    }
    return render(request, 'index-old.html', context)

def index(request):
    return render(request, 'index.html')

def counter(request):
    context = {
        'name': request.POST['name'],
        'message': request.POST['message'],
        'character_count': len(request.POST['message']),
        'word_count': len(request.POST['message'].split()),
    }
    return render(request, 'counter.html', context)

def form(request):
    context = {
        'form_action': 'counter',
        'form_method': 'POST',
        'form_input_name': 'name',
        'form_input_name_placeholder': 'Your name',
        'form_input_message': 'message',
        'form_input_message_placeholder': 'Your message',
        'form_submit_button': 'Send'
    }
    return render(request, 'form.html', context)
