from .models import Filme

def filmes_recentes(request):
    filmes = Filme.objects.all().order_by("-data_criacao")[0:8]
    return {'filmes_recentes':filmes}


def filmes_em_alta(request):
    filmes = Filme.objects.all().order_by("-visualizacoes")[0:8]
    return {'filmes_em_alta':filmes}


