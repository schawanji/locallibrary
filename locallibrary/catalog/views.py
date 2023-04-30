from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from . import models
from django.db.models import Q
#Forms
import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy

from . import forms

# Create your views here.
#@login_required
def home(request):
    #search query 
    query = request.GET.get('query')
    if query:
        books = models.Book.objects.filter(Q(title__icontains=query) | Q(author__last_name__icontains=query)| Q(author__first_name__icontains=query))
    else:
        books=[]

    #end of search query
    num_books = models.Book.objects.all().count() # num_books = models.Book.objects.count() is also ok all() is implied by default
    num_instances=models.BookInstance.objects.all().count()
    num_instances_available=models.BookInstance.objects.filter(status='a').count()
    num_authors = models.Author.objects.count()
    all_books=models.Book.objects.all()[:9]
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context={
        'query':query,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits':num_visits,
       'all_books':all_books,
       'books': books,
    }
    print(context)
    return render(request,'index.html',context=context)

class BookList(LoginRequiredMixin,ListView):
    model=models.Book
    queryset=models.Book.objects.all()[:10]
    paginate_by = 9

    def get_context_data(self, **kwargs):
        #First get the existing context from our superclass.
        context = super(BookList,self).get_context_data(**kwargs)
        #Then add your new context information.
        context['some_data']= 'This is just some data'
        #Then return the new (updated) context.
        return context
    
class BookDetail(LoginRequiredMixin,DetailView):
    model= models.Book
    template_name='catalog/book-detail.html'    

#class AuthorList(LoginRequiredMixin,ListView):
class AuthorList(LoginRequiredMixin,ListView):
    model=models.Author
    paginate_by = 10
    


class AuthorDetail(LoginRequiredMixin,DetailView):
    model=models.Author
    template_name='catalog/author-detail.html'
    
    

class LoanedBooksByUserListView(LoginRequiredMixin,ListView):
    """Generic class-based view listing books on loan to current user."""
    model = models.BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    #context_object_name='bookinstance_list'


    def get_queryset(self):
        context = (models.BookInstance.objects.filter(borrower=self.request.user).filter(status='o').order_by('due_back'))
        return context
    
class BorrowedBooksList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=models.BookInstance
    template_name='catalog/bookinstance_list_borrowed_all.html'
    paginated_by= 10
    permission_required = 'catalog.can_mark_returned'

    def get_queryset(self):
        context = (models.BookInstance.objects.filter(status='o').order_by('due_back'))
        return context

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request,pk):
    book_instance = get_object_or_404(models.BookInstance,pk=pk)
    if request.method=='POST':
        # Create a form instance and populate it with data from the request (binding):
        form = forms.RenewBookForm(request.POST)
        if form.is_valid():
           # process the data in form.cleaned_data as required (here we just write it to the model due_back field
            book_instance.due_back=form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))
        # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = forms.RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorFormCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = models.Author
    template_name='catalog/authour_form_create.html'
    permission_required = 'catalog.can_mark_returned'
    fields=['first_name','last_name','date_of_birth','date_of_death']



class AuthorFormUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.Author
    template_name='catalog/authour_form_create.html'
    permission_required = 'catalog.can_mark_returned'
    fields=['first_name','last_name','date_of_birth','date_of_death']


class AuthorFormDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = models.Author
    permission_required = 'catalog.can_mark_returned'
    #reverse_lazy() is a lazily executed version of reverse(), used here because we're providing a URL to a class-based view attribute.
    success_url = reverse_lazy('authors')
    template_name='catalog/author_confirm_delete.html'



class BookFormCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = models.Book
    template_name='catalog/book_form_create.html'
    permission_required = 'catalog.can_mark_returned'
    fields=['title', 'author','summary','isbn','genre','language','image']
    success_url = reverse_lazy('books')   
         




class BookFormUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.Book  
    template_name='catalog/book_form_create.html'
    permission_required = 'catalog.can_mark_returned'
    fields=['title', 'author','summary','isbn','genre','language','image'] 
    success_url = reverse_lazy('books')


class BookFormDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = models.Book
    template_name='catalog/book_confirm_delete.html'
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('books')
   

class BooksByAuthorListView(ListView):
    """
    View class for displaying a list of books written by a specific author.
    """
    template_name = 'catalog/books_by_author.html'
    context_object_name = 'books'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.Book.objects.filter(author__pk=pk)
       

      