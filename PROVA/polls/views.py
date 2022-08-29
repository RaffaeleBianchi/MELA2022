# django_project/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from .form import userRegistrationForm

# Create your views here.
def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = userRegistrationForm()

    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
        )
        
#from pipes import templates
from django.shortcuts import render

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

