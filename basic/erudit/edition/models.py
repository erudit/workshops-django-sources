from django.db import models


class Revue(models.Model):
    nom = models.CharField(max_length=255)

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
