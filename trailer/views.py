from django.shortcuts import render, redirect
from .models import Filme, Trailer
from django.views.generic import TemplateView, DetailView, ListView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    template_name = 'trailer/homepage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:home_filmes')
        else:
            return super().get(request, *args, **kwargs)
    
class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = 'trailer/home_filmes.html'
    model = Filme
    context_object_name = 'filmes'
    # object_list -> lista de itens do modelo
    
    
class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = 'trailer/detalhes_filme.html'
    model = Filme
    context_object_name = 'detalhes_filme'
    # object -> ' item do nosso modelo
    
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
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


class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = 'trailer/pesquisa.html'
    model = Trailer
    context_object_name = 'pesquisa'
    
    def get_queryset(self):
        obj_pesquisa = self.request.GET.get('query')
        if obj_pesquisa:
            pesquisa = self.model.objects.filter(titulo__icontains=obj_pesquisa)
            return pesquisa
        else:
            return None
    
    