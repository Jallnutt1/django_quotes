from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addQuote',views.addQuote),
    path('user/<int:user_id>',views.userQuotes),
    path('myaccount/<int:user_id>',views.myAccount),
    path('like/<int:quote_id>',views.like),
    path('unlike/<int:quote_id>',views.unlike),
    path('delete/<int:quote_id>',views.delete),
]
