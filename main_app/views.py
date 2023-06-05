from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Store
from .forms import PlayForm

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
    id_list = game.stores.all().values_list("id")
    stores_game_doesnt_have = Store.objects.exclude(id__in=id_list)
    # instantiate play form class
    play_form = PlayForm()
    return render(
        request,
        "games/detail.html",
        {"game": game, "play_form": play_form, "stores": stores_game_doesnt_have},
    )


def add_play(request, game_id):
    form = PlayForm(request.POST)
    if form.is_valid():
        new_play = form.save(commit=False)
        new_play.game_id = game_id
        new_play.save()
    return redirect("detail", game_id=game_id)


class GameCreate(CreateView):
    model = Game
    fields = "__all__"


class GameUpdate(UpdateView):
    # name your model
    model = Game
    # indicate which fields you want to be able to update.
    fields = ["type", "player_count", "description", "rating"]


class GameDelete(DeleteView):
    model = Game
    success_url = "/games"


class StoreList(ListView):
    model = Store


class StoreCreate(CreateView):
    model = Store
    fields = ["name", "type"]


class StoreDetail(DetailView):
    model = Store


def assoc_store(request, game_id, store_id):
    Game.objects.get(id=game_id).stores.add(store_id)
    return redirect("detail", game_id=game_id)


def remove_store(request, game_id, store_id):
    Game.objects.get(id=game_id).stores.remove(store_id)
    return redirect("detail", game_id=game_id)
