from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Books

# Create your views here.

class ListBooks(LoginRequiredMixin,ListView):
    template_name = "layout/listbooks.html"
    model = Books
    context_object_name = "books"


class CreateBook(CreateView):
    template_name = "layout/createbook.html"
    model = Books
    fields = ["title","author","category","pages"]
    success_url = reverse_lazy("list-book")
    context_object_name = "form"


class UpdateBook(UpdateView):
    template_name = "layout/updatebook.html"
    model = Books
    fields = ["title","author","category","pages"]
    success_url = reverse_lazy("list-book")
    context_object_name = "form"

class DeleteBook(DeleteView):
    template_name = "layout/delete.html"
    model =  Books
    success_url = reverse_lazy("list-book")
    context_object_name = "delete"