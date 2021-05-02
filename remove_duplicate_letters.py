def remove_duplicate_letters1(s: str) -> str:
    dict = {}
    a = list(s)
    s = list(s)
    while a:
        letter = a.pop()
        if letter not in dict.keys():
            dict[letter] = 1
        else:
            dict[letter] += 1

    for key, val in dict.items():
        while val > 1:
            s.remove(key)
            val -= 1

    s.sort()
    s = ''.join(s)

    return s

def