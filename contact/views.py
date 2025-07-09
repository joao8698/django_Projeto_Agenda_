from django.shortcuts import render

# Create your views here.

def inital_page(request):
    return render(request, 'contact/index.html')