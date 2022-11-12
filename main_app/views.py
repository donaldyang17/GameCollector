from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import RatingForm

# Create your views here.

def home(request):
    return render(request,'about.html')

def about(request):
    return render(request,'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request,'games/index.html', { 'games':games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    rate_form = RatingForm()
    return render(request,'games/detail.html', {'game':game, 'rate_form': rate_form})

def add_rating(request, game_id):
    form = RatingForm(request.POST)
    if form.is_valid():
        new_rating = form.save(commit=False)
        new_rating.game_id = game_id
        new_rating.save()
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = ['description']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'