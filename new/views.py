from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request,'home.html')\

def intro(request):
   return HttpResponse("Hello i am dia")

def index(request):
   person = [
      {'name': 'John', 'age': 25},
      {'name': 'Alice', 'age': 30},
      {'name': 'Bob', 'age': 35},
      {'name':'shyam','age':50},
      {'name':'ram','age':510},
      {'name':'asfds','age':50},
      {'name':'ria','age':5},
   ]
   context = {
      "name":"Hello hello",
      "age":25,
      "persons":person
   }
   return render(request,'index.html', context)

# contact, about_us .. use httpresponse
# introduction, ---create a template(intro.html) and show your introduction