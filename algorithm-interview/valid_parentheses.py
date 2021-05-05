
def is_valid(s: str) -> bool:
    stack = []
    table = {'(': ')',
             '[': ']',
             '{': '}'}

    for i in range(len(s)):
        if s[i] in table:
            stack.append(s[i])
        elif table[stack.pop()] != s[i]:
            return False

    return True