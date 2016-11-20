from django.shortcuts import render_to_response,render,get_object_or_404
from django.utils import timezone
from .models import Foto
from .forms import PostFoto
from django.shortcuts import redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse, HttpResponseRedirect


def post_list(request):
    posts = Foto.objects.filter(Fecha_Foto__lte = timezone.now()).order_by('Fecha_Foto').reverse()
    return render(request, 'crudfinal/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Foto, pk=pk)
    return render(request, 'crudfinal/post_detail.html', {'post': post})

def post_new(request):
    form = PostFoto(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit = False)
            instance.save()
            return render(request, 'crudfinal/post_edit.html', {'form': form})
    else:
        form = PostFoto()
    return render(request, 'crudfinal/post_edit.html', {'form': form})

def post_edit(request, pk):
    instance = get_object_or_404(Foto, pk=pk)
    form = PostFoto(request.POST or None, request.FILES or None , instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('crudfinal.views.post_detail', pk=instance.pk)
    return render(request, 'crudfinal/post_edit.html', {'form': form})
