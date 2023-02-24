from django.urls import path
from .views import HomePage, HomeFilmes, DetalhesFilme


app_name = 'filme'


urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='home_filmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhes_filme'),
]
