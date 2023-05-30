from django.shortcuts import render

# Create your views here.
games = [
    {
        "name": "Spirit Island",
        "type": "Co-op",
        "players": "1-6",
        "description": "Strategy co-op where players take control of elemental spirits to defend their island from foreign invaders",
        "rating": 8.4,
    },
    {
        "name": "Ark Nova",
        "type": "Strategy",
        "players": "1-4",
        "description": "Strategy game where players plan and build a modern, scientifically managed zoo",
        "rating": 8.5,
    },
]

# I want to be able to navigate to separate pages for about and all games using a navbar
# When I visit the the about page, I want to view some details about the games application
# When I visit the all page, I want to view a list of all games (index view) that displays each attribute of a game
