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
      titles = request.POST.get('title')
      descriptions = request.POST.get('description')
      
      if titles == '' and descriptions == '':
         context = {
            "error":"both field are required."
         }
         return render(request,'create.html', context)
      Note.objects.create(title = titles, descriptioin = descriptions)
      return redirect('/note')
   return render(request,'create.html')

def note_edit(request, pk):
   note = Note.objects.get(pk = pk)
   context = {
      "note" : note
   }
   if request.method == "POST":
      titles = request.POST.get('title')
      descriptions = request.POST.get('description')
      note.title = titles
      note.descriptioin = descriptions
      note.save()
      return redirect('/note')
      
   return render(request,'edit.html', context)

# def note_delete : create a function to delete a note 