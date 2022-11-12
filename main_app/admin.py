from django.contrib import admin
from .models import Game, Rating, Character

# Register your models here.

admin.site.register(Game)
admin.site.register(Rating)
admin.site.register(Character)
