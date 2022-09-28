#from pipes import templates
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
import datetime 

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
   # html = "<html><body>Hello world!.</body></html>"
    #return HttpResponse(html)
    return render(request, 'polls/index.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# django_project/users/views.py
# Create your views here.
