from django.contrib import admin
from .models import Receitas


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 30
    list_editable = ('publicada',)


admin.site.register(Receitas, ListandoReceitas)
