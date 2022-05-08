
from django.urls import include, path
from .views import *
app_name = 'notes'

urlpatterns = [
    path('',NotesListView.as_view(),name='notes'),
    path('<str:slug>',NoteDetailView.as_view(),name='note')
    
]


