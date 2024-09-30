from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil),
    path('media', views.liste_medias_membre, name='liste_medias_membre'),
    path('bibliothecaire', views.bibliothecaire, name='bibliothecaire'),
    path('bibliothecaire/membres/', views.liste_membres, name='liste_membres'),
    path('bibliothecaire/membres/creer', views.creer_membres, name='creer_membre'),
    path('bibliothecaire/membres/<int:membre_id>/modifier/', views.membre_update, name='membre_update'),
    path('bibliothecaire/membres/<int:membre_id>/supprimer/', views.membre_delete, name='membre_delete'),
    path('bibliothecaire/livres/', views.liste_livres, name='liste_livres'),
    path('bibliothecaire/livres/ajouter', views.creer_livre, name='creer_livre'),
    path('bibliothecaire/livres/<int:livre_id>/modifier/', views.livre_update, name='livre_update'),
    path('bibliothecaire/livres/<int:livre_id>/supprimer/', views.livre_delete, name='livre_delete'),
    path('bibliothecaire/dvds/', views.liste_dvds, name='liste_dvds'),
    path('bibliothecaire/dvds/ajouter', views.creer_dvd, name='creer_dvd'),
    path('bibliothecaire/dvds/<int:dvd_id>/modifier/', views.dvd_update, name='dvd_update'),
    path('bibliothecaire/dvds/<int:dvd_id>/supprimer/', views.dvd_delete, name='dvd_delete'),
    path('bibliothecaire/cds/', views.liste_cds, name='liste_cds'),
    path('bibliothecaire/cds/ajouter', views.creer_cd, name='creer_cd'),
    path('bibliothecaire/cds/<int:cd_id>/modifier/', views.cd_update, name='cd_update'),
    path('bibliothecaire/cds/<int:cd_id>/supprimer/', views.cd_delete, name='cd_delete'),
    path('bibliothecaire/jeux_de_plateau/', views.liste_jeux, name='liste_jeux'),
    path('bibliothecaire/jeux_de_plateau/ajouter', views.creer_jeu, name='creer_jeu'),
    path('bibliothecaire/jeux_de_plateau/<int:jeu_id>/modifier/', views.jeu_update, name='jeu_update'),
    path('bibliothecaire/jeux_de_plateau/<int:jeu_id>/supprimer/', views.jeu_delete, name='jeu_delete'),
    path('bibliothecaire/emprunt/', views.liste_emprunts, name='liste_emprunts'),
    path('bibliothecaire/emprunt/ajouter', views.creer_emprunt, name='creer_emprunt'),
    path('bibliothecaire/emprunt/<int:emprunt_id>/retour/', views.emprunt_return, name='emprunt_return'),
]
