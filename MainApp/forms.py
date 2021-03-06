from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta: # use the meta class because we already have a model defined called forms
        # bring in all the fields from the model Topic # we only need the text field, which is the name of the attribute
        # to create a new field for the forms that's not linked to the model, you do it before defining the metaclass
        # automatically links the model to the template
        model = Topic
        fields = ['text']
        labels = {'text':''}


class EntryForm(forms.ModelForm):
    class Meta: 
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})} 
        # modifying the look of this box # changing it to be 80 columns so it looks like a big box on the webpage