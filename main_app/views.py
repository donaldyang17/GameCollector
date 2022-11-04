from django.shortcuts import render

from django.http import HttpResponse

# Models

class Game:
    def __init__ (self, name, genre, description, publisher, release_year):
        self.name = name
        self.genre = genre
        self.description = description
        self.publisher = publisher
        self.release_year = release_year

games = [
    Game('League of Legends', 'MOBA', "Most popular game in the world.", "Riot Games", 2009),
    Game('Starcraft', 'RTS', "The first Esports game ever.", "Blizzard Entertainment", 1998),
    Game('Call of Duty: Modern Warfare 2', 'FPS',"The best game in the franchise.", "Activision", 2009),
]
# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request,'about.html')

def games_index(request):
    return render(request,'games/index.html', { 'games':games})

