from django.urls import path
from .views import ShoppingList, ShoppingDetail, ShoppingCreate, ShoppingUpdate, DeleteView

urlpatterns = [
    path('', ShoppingList.as_view(), name='shoppingList'),
    path('shoppingItem/<int:pk>', ShoppingDetail.as_view(), name='shoppingItem'),
    path('shoppingItem-create/', ShoppingCreate.as_view(), name='shoppingItem-create'),
    path('shoppingItem-update/<int:pk>', ShoppingUpdate.as_view(), name='shoppingItem-update'),
    path('shoppingItem-delete/<int:pk>', DeleteView.as_view(), name='shoppingItem-delete'),
]