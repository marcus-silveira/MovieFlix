from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, DetailView, ListView


class HomePage(TemplateView):
    template_name = 'trailer/homepage.html'

    
    
class HomeFilmes(ListView):
    template_name = 'trailer/home_filmes.html'
    model = Filme
    context_object_name = 'filmes'
    # object_list -> lista de itens do modelo
    
    
class DetalhesFilme(DetailView):
    template_name = 'trailer/detalhes_filme.html'
    model = Filme
    context_object_name = 'detalhes_filme'
    # object -> ' item do nosso modelo
    
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs)
    
    # Super classe iniciada depois pq queremos editar o método get
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filme = self.get_object()
        context['filmes_relacionados'] = Filme.objects.filter(categoria=filme.categoria).exclude(titulo=filme.titulo)
        print(context.get("filmes_relacionados"))
        context['trailers'] = filme.trailers.all()
        return context
    # Super classe iniciada antes pois queremos manter as configurações padrões e apenas adicionar novos itens
