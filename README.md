# Blog de Mitología Chilota

## Módulo
**Acceso a datos en Aplicaciones Python-Django**

## Experiencia de Aprendizaje
Actividad N°3 – Módulo 7

## Tipo
Encargo académico

---

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación web utilizando el
framework **Django** y una base de datos **PostgreSQL**, cuyo objetivo es diseñar,
implementar y consultar un modelo de datos mediante el ORM de Django.

La aplicación corresponde a un **blog cultural** enfocado en la **mitología
chilota**, donde se gestionan **autores** y **artículos** asociados a mitos
tradicionales del archipiélago de Chiloé.

El proyecto permite realizar operaciones **CRUD completas** sobre las entidades
definidas y visualizar los contenidos en una página pública con un diseño
simple y coherente con la temática cultural.

---

## Tecnologías utilizadas

- Python 3  
- Django  
- PostgreSQL  
- ORM de Django  
- HTML5  
- CSS3  
- Git y GitHub  

---

## Estructura del proyecto

```

m3-l3-blog/
│
├── blog_platform/
│   ├── blog_platform/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── blog/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── templates/
│   │   │   └── blog/
│   │   │       ├── base.html
│   │   │       └── home.html
│   │   └── static/
│   │       └── blog/
│   │           └── css/
│   │               └── style.css
│   │
│   └── manage.py
│
├── evidencias
└── README.md

```

---

## Modelos implementados

### Autor
- Nombre
- Biografía
- Región

### Artículo
- Título
- Contenido
- Mito principal
- Autor (ForeignKey)
- Fecha de creación

---

## Pasos realizados

1. Creación del proyecto Django
2. Creación de la aplicación `blog`
3. Configuración de PostgreSQL en `settings.py`
4. Definición de modelos en `models.py`
5. Ejecución de migraciones
6. Registro de modelos en el panel de administración
7. Creación de registros mediante Django Admin y Django Shell
8. Implementación de operaciones CRUD usando el ORM
9. Creación de vistas públicas
10. Implementación de templates HTML
11. Aplicación de estilos CSS
12. Visualización del blog en el navegador

---


## 📸 Evidencias – Consultas ORM en la Terminal

A continuación se presentan capturas de pantalla de la terminal que muestran
las consultas realizadas mediante el **ORM de Django** utilizando **Django Shell**.
Las consultas evidencian operaciones de lectura, filtrado y actualización
sobre los modelos definidos en la aplicación.

---

### 🔹 Acceso a Django Shell


**Consulta utilizada:**

```python
python manage.py shell
```

📷 **Evidencia:**

![Acceso a Django Shell](evidencias/orm_shell_inicio.png)
---

### 🔹 Consulta ORM – Listado de Autores (READ)

**Consulta utilizada:**

```
Autor.objects.all()
```

📷 **Evidencia:**

![Listado de Autores ORM](evidencias\orm_autores_all.png)

---

### 🔹 Consulta ORM – Listado de Artículos (READ)

**Consulta utilizada:**

```python
Articulo.objects.all()
```

📷 **Evidencia:**

![Listado de Articulos ORM](evidencias/orm_articulos_all.png)


---

### 🔹 Consulta ORM – Filtro de Artículos por Autor

**Consulta utilizada:**

```python
Articulo.objects.filter(autor__nombre__icontains="coloane")
```

📷 **Evidencia:**

![Filtro de Articulos por Autor ORM](evidencias/orm_filtro_autor.png)


---

### 🔹 Consulta ORM – Obtención de un Artículo Específico

**Consulta utilizada:**

```python
Articulo.objects.get(titulo__icontains="trauco")
```

📷 **Evidencia:**

![Get Articulo ORM](evidencias/orm_get_articulo.png)


---

### 🔹 Consulta ORM – Actualización de un Artículo (UPDATE)

**Consulta utilizada:**

```python
articulo = Articulo.objects.get(titulo__icontains="trauco")
articulo.mito_principal = "El Trauco (Mitología Chilota)"
articulo.save()
```

📷 **Evidencia:**


![Update Articulo ORM](evidencias/orm_update_articulo.png)

---

### 🔹 Consulta ORM – Eliminación de un Artículo (DELETE)



**Consulta utilizada:**
```python
Articulo.objects.filter(titulo__icontains="pincoya").delete()
```

📷 **Evidencia:**
![Delete Articulo ORM](evidencias/orm_delete_articulo.png)

---

## Autor del proyecto

**Ximena Garrido**

Proyecto académico desarrollado con fines educativos.


