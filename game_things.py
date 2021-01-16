import json


def get_info():
    with open('data\save.json') as f:
        return json.loads(f.read())


info = get_info()
game_koins = 0
