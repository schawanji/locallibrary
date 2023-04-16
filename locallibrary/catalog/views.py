from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from . import models

#Forms
import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy

from . import forms

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
    template_name='books.html'
    paginate_by = 5

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
    template_name='authors.html'
    paginate_by = 5


class AuthorDetail(LoginRequiredMixin,DetailView):
    model=models.Author
    template_name='author-detail.html'

class LoanedBooksByUserListView(LoginRequiredMixin,ListView):
    """Generic class-based view listing books on loan to current user."""
    model = models.BookInstance
    template_name = 'bookinstance_list_borrowed_user.html'
    paginate_by = 5
    #context_object_name='bookinstance_list'


    def get_queryset(self):
        context = (models.BookInstance.objects.filter(borrower=self.request.user).filter(status='o').order_by('due_back'))
        return context
    
class BorrowedBooksList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=models.BookInstance
    template_name='borrowed_books.html'
    paginated_by= 5
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
            return HttpResponseRedirect(reverse('borrowed-books'))
        # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = forms.RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'book_renew_librarian.html', context)


class AuthorFormCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = models.Author
    template_name='authour_form_create.html'
    permission_required = 'catalog.can_mark_returned'
    fields=['first_name','last_name','date_of_birth','date_of_death']


class AuthorFormUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.Author
    template_name='authour_form_create.html'
    permission_required = 'catalog.can_mark_returned'
    fields=['first_name','last_name','date_of_birth','date_of_death']


class AuthorFormDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = models.Author
    permission_required = 'catalog.can_mark_returned'
    #reverse_lazy() is a lazily executed version of reverse(), used here because we're providing a URL to a class-based view attribute.
    success_url = reverse_lazy('authors')
    template_name='author_confirm_delete.html'



class BookFormCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = models.Book
    template_name='book_form_create.html'
    permission_required = 'catalog.can_mark_returned'
    fields=['title', 'author','summary','isbn','genre']        



class BookFormUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.Book
    template_name='book_form_create.html'
    permission_required = 'catalog.can_mark_returned'
    fields=['title', 'author','summary','isbn','genre'] 


class BookFormDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = models.Book
    template_name='book_confirm_delete.html'
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('books')
   