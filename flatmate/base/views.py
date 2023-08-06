from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import ShoppingItem


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('shoppingList')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('shoppingList')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('shoppingList')
        return super(RegisterPage, self).get(*args, **kwargs)

class ShoppingList(LoginRequiredMixin, ListView):
    model = ShoppingItem
    context_object_name = 'shoppingList'
    template_name = 'base/shoppinglist.html'

    # Prevent users from seeing shopping items of other users
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoppingList'] = context['shoppingList'].filter(user=self.request.user)
        context['count'] = context['shoppingList'].filter(complete=False).count()

        search_input = self.request.GET.get("search-area") or ''
        if search_input:
            context['shoppingList'] = context['shoppingList'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context


class ShoppingDetail(LoginRequiredMixin, DetailView):
    model = ShoppingItem
    context_object_name = 'shoppingItem'
    template_name = 'base/shoppingitem.html'

class ShoppingCreate(LoginRequiredMixin, CreateView):
    model = ShoppingItem
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('shoppingList')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ShoppingCreate, self).form_valid(form)

class ShoppingUpdate(LoginRequiredMixin, UpdateView):
    model = ShoppingItem
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('shoppingList')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = ShoppingItem
    context_object_name = 'shoppingItem'
    success_url = reverse_lazy('shoppingList')
    