from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('books/',views.BookList.as_view(),name='books'),
    path('authors/',views.AuthorList.as_view(),name='authors'),
    path('book/<int:pk>', views.BookDetail.as_view(),name='book-detail'),
    path('author/<int:pk>', views.AuthorDetail.as_view(),name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]