from django.shortcuts import render_to_response,render,get_object_or_404
from django.utils import timezone
from .models import Foto, Categoria, Puntuacion
from .forms import PostFoto, PostCategoria
from django.shortcuts import redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import (CreateView,UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy


def post_list(request):
    posts = Foto.objects.filter(Fecha_Foto__lte = timezone.now()).order_by('Fecha_Foto').reverse()
    return render(request, 'crudfinal/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Foto, pk=pk)
    return render(request, 'crudfinal/post_detail.html', {'post': post})

def post_new(request):
    form = PostFoto(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit = False)
            instance.Autor_Foto = request.user
            instance.save()
            return HttpResponseRedirect('/home')
    else:
        form = PostFoto()
    return render(request, 'crudfinal/post_edit.html', {'form': form})

def post_edit(request, pk):
    instance = get_object_or_404(Foto, pk=pk)
    form = PostFoto(request.POST or None, request.FILES or None , instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.Autor_Foto = request.user
        instance.save()
        return redirect('crudfinal.views.post_detail', pk=instance.pk)
    return render(request, 'crudfinal/post_edit.html', {'form': form})

def post_delete(reques, pk = None):
    instance = get_object_or_404(Foto, pk=pk)
    instance.delete()
    redirect('crudfinal.views.post_delete')
    return HttpResponseRedirect('/home')

#Para editar, aregar y eliminar categoria. Esta seccion es exclusiva para trabajar todo respecto a categorias

def post_list_categoria(request):
    posts = Categoria.objects.order_by("Nombre_Categoria")
    return render(request, 'crudfinal/post_listar_categoria.html', {'posts': posts})

def post_detail_categoria(request, pk):
    post = get_object_or_404(Categoria, pk=pk)
    return render(request, 'crudfinal/post_detalle_categoria.html', {'post': post})

def post_new_categoria(request):
    form = PostCategoria(request.POST)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            return HttpResponseRedirect('/home/listar/categorias')
    else:
        form = PostCategoria()
    return render(request, 'crudfinal/post_edit_categoria.html', {'form': form})

def post_edit_categoria(request, pk):
    instance = get_object_or_404(Categoria, pk=pk)
    form = PostCategoria(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('crudfinal.views.post_detail_categoria', pk=instance.pk)
    return render(request, 'crudfinal/post_edit_categoria.html', {'form': form})

def post_delete_categoria(reques, pk = None):
    instance = get_object_or_404(Categoria, pk=pk)
    instance.delete()
    redirect('crudfinal.views.post_delete_categoria')
    return HttpResponseRedirect('/home/listar/categorias')
