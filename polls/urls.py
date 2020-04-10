from django.urls import path
from . import views

# This determines where you go when you just type in the basic URL (hence, the '')
# It goes to views and runs the index function
# This happens after you came through the mother urls-file in mysite already.
urlpatterns = [
    path('', views.index, name='index'),
]