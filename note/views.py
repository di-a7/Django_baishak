from django.shortcuts import render, HttpResponse, redirect
from .models import Note
# Create your views here.
def note_list(request):
   note = Note.objects.all()
   context = {
      "notes":note
   }
   return render(request,'list.html', context)


def note_create(request):
   if request.method == "POST":
      title = request.POST.get('title')
      description = request.POST.get('description')
      
      if title == '' and description == '':
         context = {
            "error":"both field are required."
         }
         return render(request,'create.html', context)
      Note.objects.create(title = title, descriptioin = description)
      return redirect('/note')
   return render(request,'create.html')
