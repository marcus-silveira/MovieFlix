from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, DetailView, ListView


class HomePage(TemplateView):
    template_name = 'trailer/homepage.html'
    
    
class HomeFilmes(ListView):
    template_name = 'trailer/home_filmes.html'
    model = Filme
    # object_list -> lista de itens do modelo
    
    
class DetalhesFilme(DetailView):
    template_name = 'trailer/detalhes_filme.html'
    model = Filme
    # object -> ' item do nosso modelo