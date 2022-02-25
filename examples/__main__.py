"""
Create and plot the examples of chaos games.
"""

import examples.sierpinski_triangle_game


# All the examples of chaos games.
games = [
    examples.sierpinski_triangle_game.SierpinskiTriangleGame,
]

# Run each game and produce the corresponding plot.
for game in games:
    game().plot()
