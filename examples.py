"""
Create and plot examples of chaos games.
"""

import pathlib
from decimal import Decimal as D

import chaos.game
import chaos.modifications


# The path for example images.
EXAMPLES_PATH = pathlib.Path("examples")
EXAMPLES_PATH.mkdir(parents=True, exist_ok=True)

# Polygons according to vertexes.
POLYGONS = {
    3: "triangle",
    4: "square",
    5: "pentagon",
    6: "hexagon",
    7: "heptagon",
    8: "octagon",
    9: "nonagon",
    10: "decagon",
    11: "hendecagon",
    12: "dodecagon",
}

# The examples games.
GAMES = [
    # Triangle games.
    chaos.game.Game(
        vertex_count=3,
        point_count=100_000,
        factor=D(1) / D(2),
    ),
    # Square games.
    chaos.game.Game(
        vertex_count=4,
        point_count=100_000,
        factor=D(1) / D(2),
        modifications=[
            chaos.modifications.IgnorePreviousVertexesModification([-1]),
        ],
    ),
    chaos.game.Game(
        vertex_count=4,
        point_count=100_000,
        factor=D(1) / D(2),
        modifications=[
            chaos.modifications.IgnoreShiftedVertexesModification([1]),
        ],
    ),
    chaos.game.Game(
        vertex_count=4,
        point_count=100_000,
        factor=D(1) / D(2),
        modifications=[
            chaos.modifications.IgnoreShiftedVertexesModification([2]),
        ],
    ),
    # Pentagon games.
    chaos.game.Game(
        vertex_count=5,
        point_count=100_000,
        factor=D(2) / (D(1) + D(5).sqrt()),
    ),
    chaos.game.Game(
        vertex_count=5,
        point_count=100_000,
        factor=D(1) / D(2),
        modifications=[
            chaos.modifications.IgnorePreviousVertexesModification([-1]),
        ],
    ),
]

for game in GAMES:
    # Games with the same number of vertexes in the original polygon.
    similar_games = [
        similar_game
        for similar_game in GAMES
        if similar_game.vertex_count == game.vertex_count
    ]

    # Construct the name, such as "triangle 1" for the first triangle game.
    game_name = "{}_{}".format(
        POLYGONS[game.vertex_count],
        similar_games.index(game) + 1,
    )

    # The PNG file to store the game plot.
    game_path = EXAMPLES_PATH / (game_name + ".png")

    print(game_name, end=": ")

    # Notify when the game has already been run.
    if game_path.exists():
        print("The image file exists. Delete the file to rerun the game.")

        continue

    # Run the game and save the plot.
    game.plot(game_path)

    print("The game plot has been saved to the image file.")
