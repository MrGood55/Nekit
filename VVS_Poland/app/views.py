from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html',{'range': range(1,12)})
def about(request):
    return render(request, 'app/about.html')