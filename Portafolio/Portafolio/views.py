from django.shortcuts import render

def inicio(request):
    return render (request, 'index.html', {})

def portafolio(request):
    return render (request, 'portafolio.html', {}) 

def formulario(request):
    return render (request, 'formulario.html,', {})