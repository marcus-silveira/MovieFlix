# Generated by Django 4.1.7 on 2023-02-24 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=1000)),
                ('thumb', models.ImageField(upload_to='thumb_trailers')),
                ('categoria', models.CharField(choices=[('TERROR', 'Terror'), ('COMEDIA', 'Comédia'), ('ACAO', 'Ação'), ('SUSPENSE', 'Suspense'), ('FICCAO', 'Ficção')], max_length=20)),
                ('visualizacoes', models.IntegerField(default=0)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
