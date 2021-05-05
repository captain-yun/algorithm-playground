# My code
def reverse_string(s: str):

    idx_from_last = len(s) - 1
    idx_from_first = 0

    for _ in range(len(s)//2):
        inter_str = s[idx_from_first]
        s[idx_from_first] = s[idx_from_last]
        s[idx_from_last] = inter_str
        idx_from_last -= 1
        idx_from_first += 1

    print(s)
    return s

# sol1
def reverse_string(s: list[str]):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left] # <--- *** You should use it
        left += 1
        right -= 1
    return s

# sol2
def reverse_string(s: list[str]):
    s.reverse() # reverse() method is only given to list.
#   s = s[::-1] # and if s is a string type, you can use it.


if __name__ == "__main__":
    reverse_string(["h","e","l","l","o"])