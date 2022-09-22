from xml.parsers.expat import model
from django import forms
from .models import Note
from django.forms.widgets import Textarea

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content"]
        widgets={'content': Textarea(attrs={'cols': 80, 'rows': 20})}