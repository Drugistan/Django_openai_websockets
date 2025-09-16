from django.shortcuts import render

def index(request):
    result={}
    print(result)
    return render(request, "chat/chat.html")
