from django.db import models

# Create your models here # table objects

class Topic(models.Model):  #inheriting all the properties of the models class
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): #returns back whatever you want it to return, instead of gibberish
        return self.text

# add a new model

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # allows us to link these two # entry is a foreign key to topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return f'{self.text[:50]}...'
    

