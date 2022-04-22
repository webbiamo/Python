from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

# Create your views here.



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()#prendi tutti gli oggetti e contali 
    num_instances = BookInstance.objects.all().count()#stessa cosa come da riga precedente

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()#qui viene utilizzata la funzione filter per contare i soli libri in status a 

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)#in questo punto del codice passiamo le variabili che abbiamo popolato attenzione il context è una funzione di python per questo richiama altro context che è la variabile. 


    # Viste come classi

from django.views import generic #occhio all'identazione detro python!!

class BookListView(generic.ListView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author