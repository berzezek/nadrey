from django.shortcuts import render

# Create your views here.
def index(request, url):
    return render(request, 'public/index.html')
