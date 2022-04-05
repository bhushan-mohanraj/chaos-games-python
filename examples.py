"""
Create and plot examples of chaos games.
"""

import pathlib
from decimal import Decimal as D

import jinja2

import chaos.game
import chaos.modifications


# The path for example images and the examples README.
EXAMPLES_PATH = pathlib.Path("examples")
EXAMPLES_PATH.mkdir(parents=True, exist_ok=True)

EXAMPLES_README_FILENAME = "README.md"
EXAMPLES_README_TEMPLATE_FILENAME = "README.md.jinja"


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


GAMES = [
    chaos.game.Game(
        vertex_count=3,
        point_count=100_000,
        factor=D(1) / D(2),
    ),
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
    chaos.game.Game(
        vertex_count=5,
        point_count=100_000,
        factor=D(1) / D(2),
        modifications=[
            chaos.modifications.IgnoreShiftedVertexesModification([-2, 2]),
        ],
    ),
    chaos.game.Game(
        vertex_count=5,
        point_count=100_000,
        factor=D(1) / D(2),
        modifications=[
            chaos.modifications.IgnoreShiftedVertexesModification([0, 1]),
        ],
    ),
    chaos.game.Game(
        vertex_count=5,
        point_count=100_000,
        factor=D(1) / D(2),
        modifications=[
            chaos.modifications.IgnoreShiftedVertexesModification([1, 2]),
        ],
    ),
    chaos.game.Game(
        vertex_count=6,
        point_count=100_000,
        factor=D(2) / D(3),
    ),
]


def get_game_name(game: chaos.game.Game) -> str:
    """
    Create a name (such as "triangle 1") for each game.
    """

    # All games with the same number of vertexes in their original polygons.
    similar_games = [
        other_game
        for other_game in GAMES
        if other_game.vertex_count == game.vertex_count
    ]

    return "{}_{}".format(
        POLYGONS[game.vertex_count],
        similar_games.index(game) + 1,
    )


def get_game_path(game: chaos.game.Game) -> pathlib.Path:
    """
    Create the path to store the plot for a game.
    """

    return EXAMPLES_PATH / (get_game_name(game) + ".png")


for game in GAMES:
    game_name = get_game_name(game)
    game_path = get_game_path(game)

    print(game_name, end=": ")

    # The environment for Jinja templates.
    template_environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader("examples"),
        autoescape=jinja2.select_autoescape(),
    )

    # Render the README template with the games.
    with (EXAMPLES_PATH / EXAMPLES_README_FILENAME).open("w") as file:
        template = template_environment.get_template(EXAMPLES_README_TEMPLATE_FILENAME)

        rendered_template = template.render(
            {
                "GAMES": GAMES,
                "get_game_name": get_game_name,
                "get_game_path": get_game_path,
            }
        )

        file.write(rendered_template)

    if game_path.exists():
        print("The image file exists. Delete the file to rerun the game.")

        continue

    game.plot(game_path)

    print("The game plot has been saved to the image file.")
