from django.shortcuts import render

def index(request):
    print("debug")
    return render(request, "chat/chat.html")
