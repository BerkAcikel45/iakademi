from django.urls import path, include

from main.views import signIn, signUp, home, updateOrder, deleteOrder, signOut

urlpatterns = [
    path('signin/', signIn, name='signIn'),
    path('signup/', signUp, name='signUp'),
    path('signout/', signOut, name='signOut'),
    path('', home, name='home'),
    path('update_order/<str:pk>/', updateOrder, name='updateOrder'),
    path('delete_order/<str:pk>/', deleteOrder, name='deleteOrder'),

]
