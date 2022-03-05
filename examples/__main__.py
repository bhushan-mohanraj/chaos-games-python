"""
Create and plot the examples of chaos games.
"""

import pathlib

import examples.sierpinski_triangle_game
import examples.sierpinski_pentagon_game


# All the examples of chaos games.
# Each tuple contains the game instance and the filename for saving.
games = [
    (
        examples.sierpinski_triangle_game.sierpinski_triangle_game,
        "sierpinski_triangle_game.png",
    ),
    (
        examples.sierpinski_pentagon_game.sierpinski_pentagon_game,
        "sierpinski_pentagon_game.png",
    ),
]

# Run each game and produce the corresponding plot.
for game, filename in games:
    game.plot(pathlib.Path(__file__).parent / filename)
