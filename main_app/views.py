from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Character
from .forms import RatingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def home(request):
    return render(request,'about.html')

def about(request):
    return render(request,'about.html')

@login_required
def games_index(request):
    games = Game.objects.filter(user=request.user)
    return render(request,'games/index.html', { 'games':games})

@login_required
def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    characters_not_added = Character.objects.exclude(id__in = game.characters.all().values_list('id'))
    rate_form = RatingForm()
    return render(request,'games/detail.html', {'game':game, 'rate_form': rate_form, 'characters': characters_not_added})

@login_required
def add_rating(request, game_id):
    form = RatingForm(request.POST)
    if form.is_valid():
        new_rating = form.save(commit=False)
        new_rating.game_id = game_id
        new_rating.save()
    return redirect('detail', game_id=game_id)

@login_required
def assoc_character(request, game_id, character_id):
  # Note that you can pass a toy's id instead of the whole object
  Game.objects.get(id=game_id).characters.add(character_id)
  return redirect('detail', game_id=game_id)

class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = ['description']

class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games/'

class CharacterList(LoginRequiredMixin, ListView):
    model = Character

class CharacterDetail(LoginRequiredMixin, DetailView):
    model = Character

class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    fields = '__all__'

class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    fields = ['description']

class CharacterDelete(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = '/characters/'