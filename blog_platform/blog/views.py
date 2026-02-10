from django.shortcuts import render
from .models import Articulo


def home(request):
    articulos = Articulo.objects.select_related("autor").order_by("-creado_en")
    return render(request, "blog/home.html", {
        "articulos": articulos
    })
