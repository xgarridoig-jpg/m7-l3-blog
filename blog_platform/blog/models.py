from django.db import models
from django.utils.text import slugify


class Autor(models.Model):
    nombre = models.CharField(max_length=120)
    biografia = models.TextField()
    region = models.CharField(max_length=100, default="Chiloé")

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="articulos"
    )
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    mito_principal = models.CharField(max_length=150)
    contenido = models.TextField()
    creado_en = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
