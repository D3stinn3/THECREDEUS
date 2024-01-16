from django.shortcuts import render

# Create your views here.

def landingPage(request):
    context = {}
    return render( request, 'base.html', context)

def examplePage(request):
    context = {}
    return render( request, 'example.html', context)