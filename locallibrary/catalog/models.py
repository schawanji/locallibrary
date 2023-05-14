from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

import uuid
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
     return self.name
    

class Language(models.Model):
   name=models.CharField(max_length=200)

   def __str__(self):
      return self.name

   
class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True,related_name='books')

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                             help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language =models.ForeignKey(Language,on_delete=models.PROTECT,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
   # Not Ideal due to many to many relationship delete later
    def display_genre(self):
       return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    image = models.ImageField(upload_to='images/',null=True)
    

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
          

class BookInstance(models.Model):
   id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
   due_back=models.DateField(null=True,blank=True)
   
   book=models.ForeignKey(Book,on_delete=models.PROTECT,null=True)
   imprint=models.CharField(max_length=200)
   borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
   LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
   status=models.CharField(max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',)
   
   class Meta:
      ordering=['due_back']
      permissions = (("can_mark_returned", "Set book as returned"),)
      
   def is_overdue(self):
    """Determines if the book is overdue based on due date and current date."""
    return bool(self.due_back and date.today() > self.due_back)   

   def _str_(self):
       return f'{self.id} ({self.book.title})'



class UserProfile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20, null=True, blank=True)
    lastname=models.CharField(max_length=20, null=True, blank=True)
    email=models.EmailField(max_length=20, null=True, blank=True)
    phone=models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/',null=True)
    

    def _str_(self):
        return f'{self.username} {self.name} {self.lastname} '