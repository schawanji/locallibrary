from django.contrib import admin
from . import models
# Register your models here.


class BookInline(admin.TabularInline):
    model=models.Book


@admin.register(models.Author)
#Above code works the same way as -> admin.site.register(models.Author,AuthorAdmin)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death','image')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'),'image']
    # Add inline listing of Books to author
   # inlines=[BookInline]

# Register the admin class with the associated model


class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance


class BookAdmin(admin.ModelAdmin):
    #Adds aditional lists to the view
    list_display = ('title','display_genre','language')
    inlines = [BooksInstanceInline]

admin.site.register(models.Book,BookAdmin)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(models.Genre)
admin.site.register(models.BookInstance,BookInstanceAdmin)
admin.site.register(models.Language)
admin.site.register(models.UserProfile)
admin.site.register(models.Country)