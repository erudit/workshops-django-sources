from django.contrib import admin

from edition.models import Editeur, Revue, Numero, Article, Auteur


admin.site.register(Editeur)
admin.site.register(Revue)
admin.site.register(Numero)
admin.site.register(Article)
admin.site.register(Auteur)
