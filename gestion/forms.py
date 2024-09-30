from django import forms
from .models import Emprunteur, Livre, CD, DVD, JeuDePlateau, Emprunt


class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['name', 'bloque']

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['name', 'auteur', 'disponible']

class CdForm(forms.ModelForm):
    class Meta:
        model = CD
        fields = ['name', 'artiste', 'disponible']

class DvdForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ['name', 'realisateur', 'disponible']

class JeuForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['name', 'createur']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['emprunteur', 'date_emprunt', 'livre', 'dvd', 'cd']

    def __init__(self, *args, **kwargs):
        super(EmpruntForm, self).__init__(*args, **kwargs)
        self.fields['emprunteur'].queryset = Emprunteur.objects.filter(bloque=False)
        self.fields['livre'].queryset = Livre.objects.filter(disponible=True)
        self.fields['dvd'].queryset = DVD.objects.filter(disponible=True)
        self.fields['cd'].queryset = CD.objects.filter(disponible=True)

    def clean(self):
        cleaned_data = super().clean()
        emprunteur = cleaned_data.get("emprunteur")
        livre = cleaned_data.get("livre")
        dvd = cleaned_data.get("dvd")
        cd = cleaned_data.get("cd")

        # Vérifiez qu'un seul champ est rempli
        if (livre is None and dvd is None and cd is None) or (livre and dvd) or (livre and cd) or (dvd and cd):
            raise forms.ValidationError("Vous devez choisir un et un seul média (livre, CD ou DVD).")

        if emprunteur:
            emprunteur.check_bloque()  # Mettre à jour l'état de l'emprunteur

