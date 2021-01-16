def get_info():
    info = {}
    with open('data\game_setting') as f:
        for i in f:
            name, value = i.strip().split('=')
            info[name] = int(value) if value.isdigit() else value
    return info


setting = get_info()
print(setting)