from sprites.funk.game import get_space_ship


def get_info():
    info = {}
    with open('data\save') as f:
        for i in f:
            name, value = i.strip().split('=')
            info[name] = int(value) if value.isdigit() else value
    return info


info = get_info()
game_koins = 0
