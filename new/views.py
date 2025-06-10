from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return HttpResponse("welcome")

def intro(request):
   return HttpResponse("Hello i am dia")

def index(request):
   return render(request,'index.html')

# contact, about_us .. use httpresponse
# introduction, ---create a template(intro.html) and show your introduction