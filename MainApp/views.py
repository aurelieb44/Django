from django.shortcuts import render, redirect
from .forms import TopicForm
from .models import Topic
# Create your views here. # Home Page

def index(request):
    return render(request, "MainApp/index.html") # rendering a page on your browser, using this template

def topics(request):
    topics = Topic.objects.order_by('-date_added') # add '-' before date for descending order
    context = {'topics':topics} # dictionary # 'topics' is the key, is what you have to refer to in the html page 
    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id): 
    topic = Topic.objects.get(id=topic_id) # Topic is a model
    entries = topic.entry_set.all() 
    context = {'topic': topic, 'entries': entries} 
    # interview question: dictionary, passes information from the view to use in the template
    # multiple objects that we need to pass # the value is what we are using in the view
    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST': 
        form = TopicForm() # load an empty form because not post request # pass the isntance to the webpage
    else: # it is a post request, we want to pass it on to the database
        form = TopicForm(data=request.POST) # I want to get the data from the post request into this variable called form
        if form.is_valid(): # if you define something as required in the model, and someone doesn't enter the info, the form won't submit
            new_topic = form.save()
            return redirect('MainApp:topics') # redirect them to the topics page
    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)

