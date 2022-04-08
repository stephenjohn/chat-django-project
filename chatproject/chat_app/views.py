from unicodedata import name
from django.shortcuts import render,redirect
from chat_app.models import Room,Message

# Create your views here.
def home(request):
    return render(request,'/Users/sangeetha/Downloads/chat/chatproject/templates/home.html')

def room(request,room):
    return render(request,'/Users/sangeetha/Downloads/chat/chatproject/templates/room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        
        
    
      

 
