from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ShoppingItem


# Create your views here.
class ShoppingList(ListView):
    model = ShoppingItem
    context_object_name = 'shoppingList'
    template_name = 'base/shoppinglist.html'


class ShoppingDetail(DetailView):
    model = ShoppingItem
    context_object_name = 'shoppingItem'
    template_name = 'base/shoppingitem.html'

class ShoppingCreate(CreateView):
    model = ShoppingItem
    fields = '__all__'
    success_url = reverse_lazy('shoppingList')

class ShoppingUpdate(UpdateView):
    model = ShoppingItem
    fields = '__all__'
    success_url = reverse_lazy('shoppingList')

class DeleteView(DeleteView):
    model = ShoppingItem
    context_object_name = 'shoppingItem'
    success_url = reverse_lazy('shoppingList')
    