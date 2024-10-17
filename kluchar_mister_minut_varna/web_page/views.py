from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def service_view(request):
    return render(request, 'service.html')


def contacts_view(request):
    return render(request, 'contact.html')


def project_view(request):
    return render(request, 'project.html')
