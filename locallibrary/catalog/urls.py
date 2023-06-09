from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('members/',views.UserProfileView.as_view(), name='members'),
    path('userprofile/<int:pk>',views.UserProfile.as_view(), name='userprofile-detail'),
    path('userprofile/create/<int:pk>',views.UserProfileCreate.as_view(), name='userprofile-create'),
    path('userprofile/update/<int:pk>',views.UserProfileUpdate.as_view(), name='userprofile-update'),
    path('userprofile/delete/<int:pk>',views.UserProfileDelete.as_view(), name='userprofile-delete'),
   
    
    path('books/',views.BookList.as_view(),name='books'),
    path('authors/',views.AuthorList.as_view(),name='authors'),
    path('signup/',views.SignupView.as_view(),name='signup'),

    path('author/<int:pk>/books/', views.BooksByAuthorListView.as_view(), name='author-books'),
    path('book/<int:pk>', views.BookDetail.as_view(),name='book-detail'),
    path('book/create', views.BookFormCreate.as_view(),name='book-create'),
    path('book/update/<int:pk>', views.BookFormUpdate.as_view(),name='book-update'),
    path('book/delete/<int:pk>', views.BookFormDelete.as_view(),name='book-delete'),

    path('author/<int:pk>', views.AuthorDetail.as_view(),name='author-detail'),
    path('author/create', views.AuthorFormCreate.as_view(),name='author-create'),
    path('author/update/<int:pk>', views.AuthorFormUpdate.as_view(),name='author-update'),
    path('author/<int:pk>/delete', views.AuthorFormDelete.as_view(),name='author-delete'),


    path('book/<uuid:pk>/borrow/',views.borrow_book,name='borrow-book-user'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.BorrowedBooksList.as_view(), name='all-borrowed'),
    #/catalog/book/<bookinstance_id>/renew/ to the function named renew_book_librarian() in views.py, and send the BookInstance id as the parameter named pk. 
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]