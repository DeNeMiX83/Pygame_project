import json

from game.funk.game import get_space_ship


def get_info():
    with open('data/save.json') as f:
        return json.loads(f.read())


info = get_info()
game_koins = 0
game_score = 0
score = 0
player = None
