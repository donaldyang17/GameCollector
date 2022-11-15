from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name="index"),
    path('games/<int:game_id>/', views.games_detail, name="detail"),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_rating/', views.add_rating, name='add_rating'),
    path('games/<int:game_id>/assoc_character/<int:character_id>/', views.assoc_character, name='assoc_character'),
    path('characters/', views.CharacterList.as_view(), name='characters_index'),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name='characters_detail'),
    path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
    path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='characters_update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='characters_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
