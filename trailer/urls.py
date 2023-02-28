from django.urls import path
from .views import HomePage, HomeFilmes, DetalhesFilme, PesquisaFilme
from django.contrib.auth import views as auth_view


app_name = 'filme'


urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='home_filmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhes_filme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisa'),
    path('login/', auth_view.LoginView.as_view(template_name='trailer/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='trailer/logout.html'), name='logout'),
]
