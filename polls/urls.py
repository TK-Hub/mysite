from django.urls import path
from . import views

# This determines where you go when you just type in the basic URL (hence, the '')
# It goes to views and runs the index function
# This happens after you came through the mother urls-file in mysite already.
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/ (Five is just a generic id here)
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# vote, results etc. are the views