from django.shortcuts import render, redirect, get_object_or_404
from .models import Livre, DVD, CD, JeuDePlateau, Emprunteur, Emprunt
from .forms import EmprunteurForm, LivreForm, CdForm, DvdForm, JeuForm, EmpruntForm

def accueil(request):
    return render(request, 'accueil.html')

def bibliothecaire(request):
    return render(request, 'bibliothecaire.html')

def liste_medias_membre(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()
    context = {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux': jeux
    }
    return render(request, 'liste_medias_membre.html', context)


# Vues pour la liste des livres, ajouter, modifier et supprimer un livre
def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'liste_livres.html', {'livres': livres})

def creer_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'creer_livre.html', {'form': form})

def livre_update(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)

    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm(instance=livre)

    return render(request, 'creer_livre.html', {'form': form})

def livre_delete(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)

    if request.method == 'POST':
        livre.delete()
        return redirect('liste_livres')

    return render(request, 'livre_confirm_delete.html', {'livre': livre})

# Vues pour la liste des DVDs, ajouter, modifier et supprimer un DVD
def liste_dvds(request):
    dvds = DVD.objects.all()
    return render(request, 'liste_dvds.html', {'dvds': dvds})

def creer_dvd(request):
    if request.method == 'POST':
        form = DvdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_dvds')
    else:
        form = DvdForm()
    return render(request, 'creer_dvd.html', {'form': form})

def dvd_update(request, dvd_id):
    dvd = get_object_or_404(DVD, pk=dvd_id)

    if request.method == 'POST':
        form = DvdForm(request.POST, instance=dvd)
        if form.is_valid():
            form.save()
            return redirect('liste_dvds')
    else:
        form = DvdForm(instance=dvd)

    return render(request, 'creer_dvd.html', {'form': form})

def dvd_delete(request, dvd_id):
    dvd = get_object_or_404(DVD, pk=dvd_id)

    if request.method == 'POST':
        dvd.delete()
        return redirect('liste_dvds')

    return render(request, 'dvd_confirm_delete.html', {'dvd': dvd})

# Vues pour la liste des CDs, ajouter, modifier et supprimer un CD
def liste_cds(request):
    cds = CD.objects.all()
    return render(request, 'liste_cds.html', {'cds': cds})

def creer_cd(request):
    if request.method == 'POST':
        form = CdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_cds')
    else:
        form = CdForm()
    return render(request, 'creer_cd.html', {'form': form})

def cd_update(request, cd_id):
    cd = get_object_or_404(CD, pk=cd_id)

    if request.method == 'POST':
        form = CdForm(request.POST, instance=cd)
        if form.is_valid():
            form.save()
            return redirect('liste_cds')
    else:
        form = CdForm(instance=cd)

    return render(request, 'creer_cd.html', {'form': form})

def cd_delete(request, cd_id):
    cd = get_object_or_404(CD, pk=cd_id)

    if request.method == 'POST':
        cd.delete()
        return redirect('liste_cds')

    return render(request, 'cd_confirm_delete.html', {'cd': cd})

# Vues pour la liste des jeux, ajouter, modifier et supprimer un jeu
def liste_jeux(request):
    jeux = JeuDePlateau.objects.all()
    return render(request, 'liste_jeux_plateau.html', {'jeux': jeux})

def creer_jeu(request):
    if request.method == 'POST':
        form = JeuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_jeux')
    else:
        form = JeuForm()
    return render(request, 'creer_jeu.html', {'form': form})

def jeu_update(request, jeu_id):
    jeu = get_object_or_404(JeuDePlateau, pk=jeu_id)

    if request.method == 'POST':
        form = JeuForm(request.POST, instance=jeu)
        if form.is_valid():
            form.save()
            return redirect('liste_jeux')
    else:
        form = JeuForm(instance=jeu)

    return render(request, 'creer_jeu.html', {'form': form})

def jeu_delete(request, jeu_id):
    jeu = get_object_or_404(JeuDePlateau, pk=jeu_id)

    if request.method == 'POST':
        jeu.delete()
        return redirect('liste_jeux')

    return render(request, 'jeu_confirm_delete.html', {'jeu': jeu})

# Vues pour la liste des membres, ajouter, modifier et supprimer un membre
def liste_membres(request):
    membres = Emprunteur.objects.all()
    return render (request, 'liste_membres.html', {'membres': membres})

def creer_membres(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = EmprunteurForm()
    return render(request, 'creer_membre.html', {'form': form})

def membre_update(request, membre_id):
    emprunteur = get_object_or_404(Emprunteur, pk=membre_id)

    if request.method == 'POST':
        form = EmprunteurForm(request.POST, instance=emprunteur)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')

    else:
        form = EmprunteurForm(instance=emprunteur)

    return render(request, 'creer_membre.html', {'form': form})

# Vue pour supprimer un membre
def membre_delete(request, membre_id):
    emprunteur = get_object_or_404(Emprunteur, pk=membre_id)

    if request.method == 'POST':
        emprunteur.delete()
        return redirect('liste_membres')

    return render(request, 'membre_confirm_delete.html', {'empreunteur': emprunteur})

def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'liste_emprunts.html', {'emprunts': emprunts})

def creer_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)  # Ne pas sauvegarder tout de suite
            # Marquer comme indisponible
            if emprunt.livre:
                emprunt.livre.disponible = False
                emprunt.livre.save()
            if emprunt.dvd:
                emprunt.dvd.disponible = False
                emprunt.dvd.save()
            if emprunt.cd:
                emprunt.cd.disponible = False
                emprunt.cd.save()
            emprunt.save()  # Sauvegarder l'emprunt
            return redirect('liste_emprunts')
    else:
        form = EmpruntForm()
    return render(request, 'creer_emprunt.html', {'form': form})


def emprunt_return(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, pk=emprunt_id)

    if request.method == 'POST':
        # Rendre le média disponible
        if emprunt.livre:
            emprunt.livre.disponible = True
            emprunt.livre.save()
        if emprunt.dvd:
            emprunt.dvd.disponible = True
            emprunt.dvd.save()
        if emprunt.cd:
            emprunt.cd.disponible = True
            emprunt.cd.save()

        # Supprimer l'emprunt
        emprunt.delete()

        # Vérifier et débloquer l'emprunteur
        emprunteur = emprunt.emprunteur
        emprunteur.check_bloque()

        return redirect('liste_emprunts')

    return render(request, 'emprunt_confirm_return.html', {'emprunt': emprunt})



