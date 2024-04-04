from django.shortcuts import render

def index(request):
    return render(request, 'f_wellness/index.html')
