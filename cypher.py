# Szyfr cezara
# Szyfr przesuwający każdy znak o x (zwykle 13) znaków "w prawo", a do odszyfrowania o x znaków "w lewo"
def get_letters():
    ret = []
    for i in range(ord('a'), ord('z') + 1):
        ret.append(chr(i))

    for i in range(ord('A'), ord('Z') + 1):
        ret.append(chr(i))

    for i in range(ord('0'), ord('9') + 1):
        ret.append(chr(i))

    ret.append(' ')
    return ret


letters = get_letters()


def caesar_encrypt(data, move_count):
    if not isinstance(data, str):
        return None

    ret = ""
    for c in data:
        ind = letters.index(c)
        ind = (ind + move_count) % len(letters)
        ret += letters[ind]

    return ret


def caesar_decrypt(data, move_count):
    if not isinstance(data, str):
        return None

    ret = ""
    for c in data:
        ind = letters.index(c) - move_count
        while ind < 0:
            ind += len(letters)

        ret += letters[ind]

    return ret
