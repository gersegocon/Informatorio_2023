from django.shortcuts import render
from .models import Noticia, Categoria
# Create your views here.
def ListarNoticias(request):
    contexto = {}
    id_categoria = request.GET.get("id", None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia=id_categoria).order_by('fecha_publicacion')
    else:
        n = Noticia.objects.all().order_by('fecha_publicacion')
    
    
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        cat = Noticia.objects.all().order_by('fecha_publicacion')

    antiguedad_des = request.GET.get("antiguedad_des")
    if antiguedad_des:
        cat = Noticia.objects.all().order_by('-fecha_publicacion')

    cat = Categoria.objects.all().order_by('nombre')

    contexto['noticias'] = n
    contexto['categorias'] = cat

    return render(request, 'noticias/listar.html', contexto)

def DetalleNoticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk = pk)
    
    contexto['noticias'] = n

    return render(request, 'noticias/detalle.html', contexto)

