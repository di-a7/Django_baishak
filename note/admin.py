from django.contrib import admin
from .models import Note
# Register your models here.

# @admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
   list_display = ['id','title','descriptioin','date']
   list_filter = ['title']
   search_fields = ('title',)
   list_editable = ('title','descriptioin')
   list_per_page = 5

admin.site.register(Note, NoteAdmin)