"""
Create and plot the examples of chaos games.
"""

import pathlib

from examples import (
    _triangle,
    _square,
    _pentagon,
)


games = {
    "triangle_sierpinski": _triangle.triangle_sierpinski_game,
    "square_1": _square.square_1_game,
    "square_2": _square.square_2_game,
    "square_3": _square.square_3_game,
    "pentagon_1": _pentagon.pentagon_1_game,
    "pentagon_sierpinski": _pentagon.pentagon_sierpinski_game,
}

for game_name, game in games.items():
    # The PNG file to store the game plot.
    game_path = pathlib.Path(__file__).parent / (game_name + ".png")

    print(game_name, end=": ")

    # Notify when the game has already been run.
    if game_path.exists():
        print("The image file exists. Delete the file to rerun the game.")

    # Run the chaos game and save the plot.
    else:
        game.plot(game_path)

        print("The game plot has been saved to the image file.")
