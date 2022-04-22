from django.urls import path
from . import views

urlpatterns = []

urlpatterns = [
    path('', views.index, name='index'),  #index è la label in ogni caso se viene cambiato il punta sempre alla label percorso lui 
    path('books/', views.BookListView.as_view(), name='books'),    
    path('authors/', views.AuthorListView.as_view(), name='authors'),                           
                                         
]

    
    
    
    
   

