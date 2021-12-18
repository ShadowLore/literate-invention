from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def philosopher1(request):
    return render(request, 'base/philosopher1.html')


def philosopher2(request):
    return render(request, 'base/philosopher2.html')


def philosopher3(request):
    return render(request, 'base/philosopher3.html')


def philosopher4(request):
    return render(request, 'base/philosopher4.html')


def philosopher5(request):
    return render(request, 'base/philosopher5.html')
