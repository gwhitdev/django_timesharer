from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.apps import apps
from blog.models import Post
from polls.models import Question
import requests

def index(request):
    external_api_data = requests.get('https://jsonplaceholder.typicode.com/photos/')
    photodata = external_api_data.json()
    photo = photodata
    three_photos = []
    
    for p in range(3):
        three_photos.append(photodata[p])

    posts = Post.objects.all()
    questions = Question.objects.all()
    context = {
        'posts': posts,
        'questions': questions,
        'photo': three_photos
    }
    return render(request, 'home/index.html', context)