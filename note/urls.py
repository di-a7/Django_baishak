from django.urls import path
from .views import *
urlpatterns = [
   path('note/', note_list),
   path('note/create/',note_create),
   path('note/<pk>/edit', note_edit),
]

