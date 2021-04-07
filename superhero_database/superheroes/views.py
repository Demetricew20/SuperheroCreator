from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Superhero
from django.forms import ModelForm


class SuperheroForm(ModelForm):
    class Meta:
        model = Superhero
        fields = ['hero_name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase']


# Create your views here.

def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    selected_superhero = get_object_or_404(Superhero, pk=superhero_id)
    context = {
        'selected_superhero': selected_superhero
    }

    return render(request, 'superheroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        hero_name = request.POST.get('hero_name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(hero_name=hero_name, alter_ego=alter_ego, primary_ability=primary_ability,
                                  secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def edit(request, superhero_id):
    superhero = get_object_or_404(Superhero, pk=superhero_id)

    form = SuperheroForm(request.POST or None, instance=superhero)

    if form.is_valid():
        form.save()
        return redirect('superheroes:index')

    context = {
        'form': form
    }

    return render(request, 'superheroes/edit.html', context)


def delete(request, superhero_id):
    superhero = get_object_or_404(Superhero, pk=superhero_id)
    if request.method == 'POST':
        superhero.delete()
        return redirect('superheroes:index')

    context = {
        'superhero': superhero
    }

    return render(request, 'superheroes/delete.html', context)
