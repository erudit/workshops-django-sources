from django.db import models


class Editeur(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Revue(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Numero(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Article(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    date_naissance = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nom
