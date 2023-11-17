from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .models import Words


class HomeTemplateView(TemplateView):
    template_name = 'main/home.html'
    extra_context = {'title': 'My dictionary'}


class WordsListView(ListView):
    model = Words
    extra_context = {'title': 'Word\'s dictionary'}
    template_name = 'main/words.html'
    context_object_name = 'words'


class WordCreateView(CreateView):
    model = Words
    fields = '__all__'
    template_name = 'main/addword.html'
    extra_context = {'title': 'Add word'}
    success_url = reverse_lazy('home')