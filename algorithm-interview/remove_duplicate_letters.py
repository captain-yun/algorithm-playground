def remove_duplicate_letters1(s: str) -> str:
    # cbacdcbc

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

def remove_duplicate_letters(s: str) -> str:
    answer = ''
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(suffix) == set(s):
            s = char + suffix