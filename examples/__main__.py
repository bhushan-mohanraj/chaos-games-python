"""
Create and plot the examples of chaos games.
"""

import pathlib

import examples._triangle
import examples._pentagon


games = {
    "triangle_sierpinski": examples._triangle.triangle_sierpinski_game,
    "pentagon_sierpinski": examples._pentagon.pentagon_sierpinski_game,
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
