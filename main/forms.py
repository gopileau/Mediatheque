from django import forms
from .models import Livre, DVD, Cd, JeuDePlateau, Emprunt, Member


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['name', 'auteur', 'disponible']

class DvdForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ['name', 'realisateur', 'disponible']

class CdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = ['name', 'artiste', 'disponible']

class JeuDePlateauForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['name', 'createur']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['membre', 'media']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'bloque']
