from django import forms
from . models import Task
class ToDoForm (forms.ModelForm):
    class Meta:
        model=Task
        fields = ['title' ,'description' , 'due_date' , 'due_time']
        widgets = {
            'title' : forms.TextInput(),
            'description' : forms.Textarea(),
            'due_date' : forms.DateInput(attrs={'type' : 'date'}),
            'due_time' : forms.TimeInput(attrs={'type' : 'time'}),
        }
        