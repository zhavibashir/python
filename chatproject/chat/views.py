from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
# Create your views here.
@login_required
def home(request):
    users = User.objects.all()
    return render(request, 'chat/index.html', {"users" : users})

def messages(request):
    from_user = User.objects.filter(username="yuujey").first()
    from_messages = Message.objects.filter(to_user = request.user, from_user=from_user).values()

    to_messages = Message.objects.filter(from_user = request.user, to_user=from_user).values()
    data = {"messages": [list(from_messages), list(to_messages)]}


    return JsonResponse(data)