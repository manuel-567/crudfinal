from django.shortcuts import render_to_response,render

#def home(request):
#    return render_to_response('index.html')
def post_list(request):
    return render(request, 'crudfinal/post_list.html', {})
