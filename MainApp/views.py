from django.shortcuts import render
from .models import Topic
# Create your views here. # Home Page

def index(request):
    return render(request, "MainApp/index.html") # rendering a page on your browser, using this template

def topics(request):
    topics = Topic.objects.all() # add '-' before date for descending order
    context = {'topics':topics} # dictionary # 'topics' is the key, is what you have to refer to in the html page 
    return render(request, 'MainApp/topics.html', context)
