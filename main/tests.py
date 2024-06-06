from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from .models import Livre, Emprunt, Member, JeuDePlateau


class LivreModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.member = Member.objects.create(user=self.user)
        self.livre = Livre.objects.create(name='Test Livre', auteur='Auteur Test', disponible=True)

    def test_livre_creation(self):
        self.assertEqual(self.livre.name, 'Test Livre')
        self.assertEqual(self.livre.auteur, 'Auteur Test')
        self.assertTrue(self.livre.disponible)

    def test_emprunt_creation(self):
        emprunt = Emprunt.objects.create(membre=self.member, media=self.livre)
        self.assertEqual(emprunt.membre.user.username, 'testuser')
        self.assertEqual(emprunt.media.name, 'Test Livre')

    def test_member_creation(self):
        self.assertEqual(self.member.user.username, 'testuser')
        self.assertFalse(self.member.bloque)

    def test_max_emprunts(self):
        for _ in range(3):
            Emprunt.objects.create(membre=self.member, media=self.livre)

        emprunt = Emprunt(membre=self.member, media=self.livre)
        with self.assertRaises(ValidationError):
            emprunt.clean()

    def test_emprunt_retard(self):
        emprunt = Emprunt.objects.create(membre=self.member, media=self.livre)
        emprunt.date_emprunt = timezone.now() - timedelta(weeks=2)  # Simulate an overdue loan
        with self.assertRaises(ValidationError):
            emprunt.clean()

    def test_emprunt_jeu_de_plateau(self):
        jeu_de_plateau = JeuDePlateau.objects.create(name='Test Jeu', createur='Createur Test')
        emprunt = Emprunt(membre=self.member, media=jeu_de_plateau)
        with self.assertRaises(ValidationError):
            emprunt.clean()

    def test_retour_emprunt(self):
        emprunt = Emprunt.objects.create(membre=self.member, media=self.livre)
        emprunt.date_retour = timezone.now()
        emprunt.save()
        self.assertIsNotNone(emprunt.date_retour)
