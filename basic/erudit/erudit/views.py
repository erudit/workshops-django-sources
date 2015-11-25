from django.shortcuts import render

def home(request):
    c = {
        'revue': "L'Actualité économique",
    }
    return render(request, 'home.html', c)
