from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analysis(request):
    return render(request, 'analysis.html')


def device(request):
    return render(request, 'device.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')
