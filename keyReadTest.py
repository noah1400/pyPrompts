from msvcrt import getch

while True:
    key = getch()
    if key == ' ':
        break
    key = (key, )
    if (key[0] == b'\x00' or key[0] == b'\xe0'):
        key = (key[0], getch())

    print(key)