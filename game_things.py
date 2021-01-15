def get_info():
    info = {}
    with open('data\save') as f:
        for i in f:
            name, value = i.strip().split('=')
            info[name] = int(value)
    return info


info = get_info()
koins = 0