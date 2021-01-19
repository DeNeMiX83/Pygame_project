import json


def get_info():
    with open('data\game_setting.json') as f:
        return json.loads(f.read())


setting = get_info()