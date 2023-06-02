from django.shortcuts import render
from .models import Game

# Create your views here.
# games = [
#     {
#         "name": "Spirit Island",
#         "type": "Co-op",
#         "players": "1-6",
#         "description": "Strategy co-op where players take control of elemental spirits to defend their island from foreign invaders",
#         "rating": 8.4,
#     },
#     {
#         "name": "Ark Nova",
#         "type": "Strategy",
#         "players": "1-4",
#         "description": "Strategy game where players plan and build a modern, scientifically managed zoo",
#         "rating": 8.5,
#     },
# ]


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def games_index(request):
    games = Game.objects.all()
    return render(request, "games/index.html", {"games": games})


# respond to request to games_detail, pass in request and game_id
def games_detail(request, game_id):
    # create a game variable and assign it to the game objects id
    game = Game.objects.get(id=game_id)
    return render(request, "games/details.html", {"game": game})


# [x] I want to be able to navigate to separate pages for about and all games using a navbar
# [x] When I visit the the about page, I want to view some details about the games application
# [ ] When I visit the all page, I want to view a list of all games (index view) that displays each attribute of a game
