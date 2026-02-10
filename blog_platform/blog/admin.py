from django.contrib import admin
from .models import Autor, Articulo


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "region")
    search_fields = ("nombre", "region")


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "mito_principal", "autor", "creado_en")
    list_filter = ("mito_principal", "creado_en")
    search_fields = ("titulo", "mito_principal", "autor__nombre")
    prepopulated_fields = {"slug": ("titulo",)}
