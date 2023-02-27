from django.db import models
from django.utils import timezone


LISTA_CATEGORIAS = (
    ('TERROR', 'Terror'),
    ('COMEDIA', 'Comédia'),
    ('ACAO', 'Ação'),
    ('SUSPENSE', 'Suspense'),
    ('FICCAO', 'Ficção')
    )

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    thumb = models.ImageField(upload_to='thumb_trailers')
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.titulo
    
    
class Trailer(models.Model):
    filme = models.ForeignKey('Filme', related_name='trailers', on_delete=models.CASCADE)
    thumb = models.ImageField(upload_to='thumb_trailers', null=True)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    def __str__(self):
        return self.titulo