from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
def home(request):
    num_books = models.Book.objects.all().count()
    num_instances=models.BookInstance.objects.all().count()
    num_instances_available=models.BookInstance.objects.filter(status='a').count()
    num_authors = models.Author.objects.count()
    context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request,'index.html',context=context)

class BookList(ListView):
    model=models.Book
    context_object_name='book_list'
    queryset=models.Book.objects.all()[:10]
    template_name='book.html'

    def get_context_data(self, **kwargs):
        #First get the existing context from our superclass.
        context = super(BookList,self).get_context_data(**kwargs)
        #Then add your new context information.
        context['some_data']= 'This is just some data'
        #Then return the new (updated) context.
        return context
    
class BookDetail(DetailView):
    model= models.Book
    template_name='book-detail.html'    

class AuthorList(ListView):
    model=models.Author
    context_object_name='author_list'
    template_name='author.html'

    
class AuthorDetail(DetailView):
    model=models.Author
    template_name='author-detail.html'