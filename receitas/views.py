from django.shortcuts import get_object_or_404, render
from .models import Receitas


def index(request):
    receitas = Receitas.objects.order_by(
        '-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    link_receita = {
        'receita': receita
    }
    return render(request, 'receita.html', link_receita)


def buscar(request):
    lista_receitas = Receitas.objects.order_by(
        '-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(
                nome_receita__icontains=nome_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)
