from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Livre, DVD, Cd, JeuDePlateau, Emprunt, Member
from .forms import LivreForm, DvdForm, CdForm, JeuDePlateauForm, EmpruntForm, MemberForm
from django.utils import timezone
from django.shortcuts import render

@login_required
def menu_member(request):
    return render(request, 'main/menu_member.html')
@login_required
def index(request):
    return render(request, 'main/index.html')
@login_required
def member_list(request):
    members = Member.objects.all()
    return render(request, 'main/member_list.html', {'members': members})
@login_required
def menu_bibliotheque(request):
    return render(request, 'main/menu_bibliotheque.html')
@login_required
def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'main/create_member.html', {'form': form})

@login_required
def create_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = LivreForm()
    return render(request, 'main/create_livre.html', {'form': form})

@login_required
def create_dvd(request):
    if request.method == 'POST':
        form = DvdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = DvdForm()
    return render(request, 'main/create_dvd.html', {'form': form})

@login_required
def create_cd(request):
    if request.method == 'POST':
        form = CdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = CdForm()
    return render(request, 'main/create_cd.html', {'form': form})

@login_required
def create_jeu_de_plateau(request):
    if request.method == 'POST':
        form = JeuDePlateauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = JeuDePlateauForm()
    return render(request, 'main/create_jeu_de_plateau.html', {'form': form})

@login_required
def media_list(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = Cd.objects.all()
    jeux_de_plateau = JeuDePlateau.objects.all()
    return render(request, 'main/media_list.html', {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux_de_plateau': jeux_de_plateau,
    })

@login_required
def create_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            try:
                form.clean()
                form.save()
                return redirect('media_list')
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        form = EmpruntForm()
    return render(request, 'main/create_emprunt.html', {'form': form})

@login_required
def update_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'main/update_member.html', {'form': form})

@login_required
def return_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    emprunt.date_retour = timezone.now()
    emprunt.save()
    return redirect('media_list')

@login_required
def emprunt_list(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'main/emprunt_list.html', {'emprunts': emprunts})
