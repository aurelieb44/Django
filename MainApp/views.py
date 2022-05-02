from django.shortcuts import render, redirect
from .forms import EntryForm, TopicForm
from .models import Entry, Topic
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

def new_entry(request, topic_id): # topic_id to identify what topic it is # topic_id is just an integer
    topic = Topic.objects.get(id=topic_id) # topic object
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # the only field that will show up on the webpage is text
            # the entry model has 3 fields: topic, text, date_added(automatic)
            # before we save it, that field is a required field
            # we are not saving it to the database # ready to save but not write yet to the database
            new_entry.topic = topic # from line 34
            new_entry.save()
            return redirect('MainApp:topic', topic_id=topic_id) # what page do we want to load after: the topic page with all the entries showing
            # to load the topic page, you need the topic_id
            # orange in the urls.py file, white in line 34 # what you pass is not an object, it's just an id
    context = {'form':form, 'topic':topic} # we pass topic and form
    return render(request, 'MainApp/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id) # calling the entry object/model
    topic = entry.topic # calling the entry of that topic # topic is an attribute 
    # lower case entry because this is the avriable that is storing that particular object
    if request.method != 'POST':
        form = EntryForm(instance=entry) # we want to grab that particular instance # will load existing data for that entry
    else:
        form = EntryForm(instance=entry, data=request.POST) # take the data on the webpage and put that in the database
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id) # redirect to that topic page 
    context = {'form':form, 'topic':topic, 'entry': entry} # we pass topic, form and entry # dictionary is growing, passing multiple objects at the same time
    return render(request, 'MainApp/edit_entry.html', context)