

class Key:

    CTRL_B = (b'\x02',)

    CTRL_F = (b'\x06',)

    CTRL_A = (b'\x01',)

    CTRL_E = (b'\x05',)

    CTRL_U = (b'\x15',)

    CTRL_C = (b'\x03',)

    LEFT = (b'\x00', b'K')

    LEFT_ARROW = (b'\x00', b'K')

    RIGHT = (b'\x00', b'M')

    RIGHT_ARROW = (b'\x00', b'M')

    HOME = (b'\xe0', b'G')

    END = (b'\xe0', b'O')

    DELETE = (b'\xe0', b'S')

    ENTER = (b'\r',)

    BACKSPACE = (b'\x08',)

    KEYS = {
        CTRL_B,
        CTRL_F,
        CTRL_A,
        CTRL_E,
        CTRL_U,
        CTRL_C,
        LEFT,
        LEFT_ARROW,
        RIGHT,
        RIGHT_ARROW,
        HOME,
        END,
        DELETE,
        ENTER
    }

    def isDefined(key: tuple) -> bool:
        ret = (key in Key.KEYS)
        return ret


    