from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Note
from .forms import NoteForm
# Create your views here.
# i added this comment to see github
def home(request):
    all_notes = Note.objects.all()
    form = NoteForm()
    context = {"all_notes":all_notes, "form":form}
    
    return render(request, 'notesapp/index.html', context)

def add(request):
    new_note = Note(title=request.POST['title'], content= request.POST['content'])
    new_note.save()

    data = {"title": new_note.title,
    "content":new_note.content,
    "date":new_note.date}
    return JsonResponse(data)

def search(request):
    all_notes = Note.objects.filter(title__contains=request.POST['title']).values()
    # form = NoteForm()
    data ={"notes": list(all_notes)}
    return JsonResponse(data)