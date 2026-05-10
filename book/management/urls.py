from django.urls import path, include

from .views import ListBooks,CreateBook,UpdateBook,DeleteBook

urlpatterns = [
    path("",ListBooks.as_view(),name="list-book"),
    path("create",CreateBook.as_view(),name="create-book"),
    path("update/<int:pk>",UpdateBook.as_view(),name="update-book"),
    path("delete/<int:pk>",DeleteBook.as_view(),name="delete-book"),
    path("accounts/",include("django.contrib.auth.urls"))
]
