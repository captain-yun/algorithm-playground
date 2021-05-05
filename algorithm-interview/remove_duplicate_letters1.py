def remove_duplicate_letters1(s: str) -> str:
    # cbacdcbc
    # put every s into key
    answer = ''
    ht = {}
    for char in s:
        if char not in ht.keys():
            ht[char] = 1
        else:
            ht[char] += 1

    for char in sorted(set(s)):
        stack = []
        stack = list(s[:s.index(char)])
        n = len(stack)
        temp_ht = ht.copy()

        while n > 0:
            v = stack.pop()
            if temp_ht[v] > 1:
                n -= 1
                temp_ht[v] -= 1
            else:
                break

        if n == 0:
            ht = temp_ht.copy()
            ht[char] -= 1
            answer += s[s.index(char)]
            s = s[s.index(char)+1:]
    return answer


def remove_duplicate_letters(s: str) -> str:
    answer = ''
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(suffix) == set(s):
            s = char + suffix