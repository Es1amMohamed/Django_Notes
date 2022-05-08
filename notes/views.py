from datetime import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.
class NotesListView(ListView):
    
    model = Note
    
class NoteDetailView(DetailView):
    
    model = Note

        
    

