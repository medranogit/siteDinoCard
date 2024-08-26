from django.shortcuts import render

def index(request):
    return render(request, 'myApp/index.html')

def teste(request):
    return render(request, 'myApp/teste.html')  # Adiciona o view para renderizar o template 'teste.html'