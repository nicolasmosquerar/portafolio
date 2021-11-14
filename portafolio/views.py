from django.shortcuts import render

from portafolio.models import proyecto


def home(request):
    projects = proyecto.objects.all()
    return render(request, 'home.html', {'projects': projects})


