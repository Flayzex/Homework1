from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('home', views.HomeTemplateView.as_view(), name='home'),
    path('words_list', views.WordsListView.as_view(), name='words-list'),
    path('add_word', views.WordCreateView.as_view(), name='add-word')
]
