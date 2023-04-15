from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

# Create your views here.
@login_required
def home(request):
    num_books = models.Book.objects.all().count() # num_books = models.Book.objects.count() is also ok all() is implied by default
    num_instances=models.BookInstance.objects.all().count()
    num_instances_available=models.BookInstance.objects.filter(status='a').count()
    num_authors = models.Author.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits':num_visits,
    }
    return render(request,'index.html',context=context)

class BookList(LoginRequiredMixin,ListView):
    model=models.Book
    context_object_name='book_list'
    queryset=models.Book.objects.all()[:10]
    template_name='book.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        #First get the existing context from our superclass.
        context = super(BookList,self).get_context_data(**kwargs)
        #Then add your new context information.
        context['some_data']= 'This is just some data'
        #Then return the new (updated) context.
        return context
    
class BookDetail(LoginRequiredMixin,DetailView):
    model= models.Book
    template_name='book-detail.html'    

class AuthorList(LoginRequiredMixin,ListView):
    model=models.Author
    context_object_name='author_list'
    template_name='author.html'
    paginate_by = 2


class AuthorDetail(LoginRequiredMixin,DetailView):
    model=models.Author
    template_name='author-detail.html'