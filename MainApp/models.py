from django.db import models

# Create your models here # table objects

class Topic(models.Model):  #inheriting all the properties of the models class
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): #returns back whatever you want it to return, instead of gibberish
        return self.text
        

