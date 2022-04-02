"""
Create and plot the examples of chaos games.
"""

import pathlib

import examples._triangle
import examples._pentagon


game_filenames = {
    "triangle_sierpinski.png": examples._triangle.sierpinski_triangle_game,
    "pentagon_sierpinski.png": examples._pentagon.sierpinski_pentagon_game,
}

# Run each game and produce the corresponding plot.
for filename, game in game_filenames.items():
    game.plot(pathlib.Path(__file__).parent / filename)
