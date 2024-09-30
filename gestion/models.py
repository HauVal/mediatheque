from datetime import timezone
from django.utils import timezone
from django.db import models

#Classe abstraite pour que les autres classe hérite de celle ci
class Media(models.Model):
    name = models.fields.CharField(max_length=120)
    date_emprunt = models.fields.DateField(null=True, blank=True)
    disponible = models.fields.BooleanField(default=True)
    emprunteur = models.ForeignKey('Emprunteur', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Livre(Media):
    auteur = models.fields.CharField(max_length=120)

class DVD(Media):
    realisateur = models.fields.CharField(max_length=120)

class CD(Media):
    artiste = models.fields.CharField(max_length=120)

class JeuDePlateau(models.Model):
    name = models.fields.CharField(max_length=120)
    createur = models.fields.CharField(max_length=120)

    def __str__(self):
        return self.name

class Emprunteur(models.Model):
    name = models.CharField(max_length=120)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def count_emprunts(self):
        # Sert à compter le nombre d'emprunt pour l'afficher dans la liste des membres
        return Emprunt.objects.filter(emprunteur=self).count()


    def check_bloque(self):
        # Sert à compter le nombre d'emprunt pour savoir à quel moment bloqué le membre.
        emprunts_actifs = Emprunt.objects.filter(emprunteur=self)
        # BLoque le membre après le 3ème emprunt
        if emprunts_actifs.count() >= 2:
            if not self.bloque:
                self.bloque = True
                self.save()
            return True

        # Vérifier les emprunts de plus de 7 jours
        for emprunt in emprunts_actifs:
            if (timezone.now().date() - emprunt.date_emprunt).days > 7:
                if not self.bloque:
                    self.bloque = True
                    self.save()
                return True

        if self.bloque:  # Débloquer si nécessaire
            self.bloque = False
            self.save()
        return False

class Emprunt(models.Model):
    emprunteur = models.ForeignKey('Emprunteur', on_delete=models.SET_NULL, null=True)
    date_emprunt = models.fields.DateField(default=timezone.now, null=True)
    livre = models.ForeignKey("Livre", on_delete=models.SET_NULL, null=True, blank=True)
    dvd = models.ForeignKey("DVD", on_delete=models.SET_NULL, null=True, blank=True)
    cd = models.ForeignKey("CD", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        emprunteur_name = self.emprunteur.name if self.emprunteur else 'Inconnu'
        date = self.date_emprunt if self.date_emprunt else 'Date inconnue'
        livre_name = self.livre.name if self.livre else ''
        dvd_name = self.dvd.name if self.dvd else ''
        cd_name = self.cd.name if self.cd else ''

        return f"{emprunteur_name} {livre_name}{dvd_name}{cd_name} {date}"


