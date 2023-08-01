from django.urls import path
from .views import ShoppingList, ShoppingDetail, ShoppingCreate, ShoppingUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ShoppingList.as_view(), name='shoppingList'),
    path('shoppingItem/<int:pk>', ShoppingDetail.as_view(), name='shoppingItem'),
    path('shoppingItem-create/', ShoppingCreate.as_view(), name='shoppingItem-create'),
    path('shoppingItem-update/<int:pk>', ShoppingUpdate.as_view(), name='shoppingItem-update'),
    path('shoppingItem-delete/<int:pk>', DeleteView.as_view(), name='shoppingItem-delete'),
]