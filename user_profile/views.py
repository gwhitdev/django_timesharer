from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.
def index(request):
    context = {}
    return render(request, 'user_profile/index.html', context)
