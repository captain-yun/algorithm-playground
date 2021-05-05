# def most_common_word(paragraph :str, banned: list[str]):
#     paragraph = paragraph.split(" ,.")
#     most_common = {}
#     for word in paragraph:
#         if most_common[word]:
#             most_common[word] = 1
#         else:
#             most_common[word] += 1


import re
def most_common_word_1(paragraph :str, banned: list[str]):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    print(words)

    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    print(words)


if __name__ == "__main__":
    most_common_word_1(["h","e","l","l","o"])