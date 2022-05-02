import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()
from MainApp.models import Topic
topics = Topic.objects.all() # we are getting all the topic objects (chess, rock climbing)

for t in topics:
    print(t.id, ' ', t) # id is an attribute of the topic object

t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)

entries = t.entry_set.all() # get all the entries for a specific topic # get data through a FK relationship 
# topic is a FK attribute in the entry model
for e in entries:
    print(e)
