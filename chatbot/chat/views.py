from django.shortcuts import render,redirect
from chat.models import Room,Messages
# Create your views here.
from django.http import HttpResponse,JsonResponse


def home(request):
    return render(request,'home.html')
def room(request,room):
    username = request.GET.get('usernmae')
    room_details = Room.objects.get(name=room)
    return render(request,'room.html',{'username':username,
    'room':room,
     'room_details':room_details})
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Messages.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Messages.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


