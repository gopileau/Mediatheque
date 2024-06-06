from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Media(models.Model):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('dvd', 'DVD'),
        ('cd', 'CD'),
        ('jeu_de_plateau', 'Jeu de Plateau'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Emprunt(models.Model):
    membre = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.membre.username} a emprunté {self.media.name}"

    def clean(self):
        if self.membre.emprunt_set.filter(date_retour__isnull=True).count() >= 3:
            raise ValidationError("Un membre ne peut pas avoir plus de 3 emprunts à la fois.")
        if self.date_emprunt + timedelta(weeks=1) < timezone.now() and self.date_retour is None:
            raise ValidationError("Emprunt en retard. Impossible de créer un nouvel emprunt.")
        if self.media.type == 'jeu_de_plateau':
            raise ValidationError("Les jeux de plateau ne peuvent pas être empruntés.")

class Livre(models.Model):
    name = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    date_emprunt = models.DateTimeField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='livres')

    def __str__(self):
        return self.name

class DVD(models.Model):
    name = models.CharField(max_length=255)
    realisateur = models.CharField(max_length=255)
    date_emprunt = models.DateTimeField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='dvds')

    def __str__(self):
        return self.name

class Cd(models.Model):
    name = models.CharField(max_length=255)
    artiste = models.CharField(max_length=255)
    date_emprunt = models.DateTimeField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='cds')

    def __str__(self):
        return self.name

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=255)
    createur = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
