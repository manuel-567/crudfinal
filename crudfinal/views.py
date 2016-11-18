from django.shortcuts import render_to_response,render,get_object_or_404
from django.utils import timezone
from .models import Foto



def post_list(request):
    posts = Foto.objects.filter(Fecha_Foto__lte = timezone.now()).order_by('Fecha_Foto')
    return render(request, 'crudfinal/post_list.html', {'posts': posts})
#def home(request):
#    return render_to_response('index.html')
#def post_list(request):
#    return render(request, 'crudfinal/post_list.html', {})
def post_detail(request, pk):
        post = get_object_or_404(Foto, pk=pk)
        return render(request, 'crudfinal/post_detail.html', {'post': post})
