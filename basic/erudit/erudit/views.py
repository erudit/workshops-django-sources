from django.shortcuts import render

from edition.models import Revue

def home(request):

    revues = Revue.objects.all()

    c = {
        'revues': revues,
    }
    return render(request, 'home.html', c)
