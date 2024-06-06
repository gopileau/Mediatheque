from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('media_list/', views.media_list, name='media_list'),
    path('create_livre/', views.create_livre, name='create_livre'),
    path('create_dvd/', views.create_dvd, name='create_dvd'),
    path('create_cd/', views.create_cd, name='create_cd'),
    path('create_jeu_de_plateau/', views.create_jeu_de_plateau, name='create_jeu_de_plateau'),
    path('create_member/', views.create_member, name='create_member'),
    path('create-emprunt/', views.create_emprunt, name='create_emprunt'),
    path('update_member/<int:pk>/', views.update_member, name='update_member'),
    path('return_emprunt/<int:pk>/', views.return_emprunt, name='return_emprunt'),
    path('menu_member/', views.menu_member, name='menu_member'),  # Ajoutez cette ligne
    path('menu/', views.menu_bibliotheque, name='menu_bibliotheque'),
    path('member-list/', views.member_list, name='member_list'),
    path('emprunt_list/', views.emprunt_list, name='emprunt_list'),
]








