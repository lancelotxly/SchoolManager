from django.shortcuts import render,redirect,HttpResponse

def index(req):
    return render(req,'main.html')