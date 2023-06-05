from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("games/", views.games_index, name="index"),
    path("games/<int:game_id>/", views.games_detail, name="detail"),
    path("games/create/", views.GameCreate.as_view(), name="games_create"),
    path("games/<int:pk>/update/", views.GameUpdate.as_view(), name="games_update"),
    path("games/<int:pk>/delete/", views.GameDelete.as_view(), name="games_delete"),
    path("games/<int:game_id>/add_play/", views.add_play, name="add_play"),
    path("stores/", views.StoreList.as_view(), name="stores_index"),
    path("stores/<int:pk>/", views.StoreDetail.as_view(), name="stores_detail"),
    path("stores/create/", views.StoreCreate.as_view(), name="stores_create"),
    path(
        "games/<int:game_id>/assoc_store/<int:store_id>/",
        views.assoc_store,
        name="assoc_store",
    ),
    path(
        "games/<int:game_id>/remove_store/<int:store_id>/",
        views.remove_store,
        name="remove_store",
    ),
]
