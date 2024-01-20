from django.shortcuts import render


# Create your views here.

def landingPage(request):
    context = {}
    return render(request, 'template/index.html', context)

def homePage(request):
    context = {}
    return render(request, 'template/home.html', context)

def worksPage(request):
    context = {}
    return render(request, 'template/works.html', context)

def contactPage(request):
    context = {}
    return render(request, 'template/contact.html', context)

def portfolioPage(request):
    context = {}
    return render(request, 'template/portfolio.html', context)