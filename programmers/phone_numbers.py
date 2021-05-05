# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#
#     for i in range(len(phone_book) - 1):
#         for j in range(i + 1, len(phone_book)):
#             if len(phone_book[i]) < len(phone_book[j]):
#                 if phone_book[j].find(phone_book[i]):
#                     return False
#             else:
#                 if phone_book[i][:len(phone_book[j])] == phone_book[j]:
#                     return False
#     return True
#
#
# def solution1(phone_book):
#     answer = True
#     phone_book.sort(key=len)
#     min_len = len(phone_book[0])
#     max_len = len(phone_book[-1])
#
#     # for i in range(len(phone_book) - 1, min_len + 1, -1):
#     i = len(phone_book) - 1
#     j = 0
#     while len(phone_book[i]) > min_len:
#         while len(phone_book[j]) < len(phone_book[i]):
#             if phone_book[i].find(phone_book[j]) >= 0:
#                 return False
#             j += 1
#         i -= 1
#         j = 0
#     return True


# def solution2(phone_book):
#     answer = True
#     # phone_book.sort(key=len)    min_len = len(phone_book[0])
#     max_len = len(phone_book[-1])
#
#
#     i = len(phone_book) - 1
#     j = 0
#     while len(phone_book[i]) > min_len:
#         while len(phone_book[j]) < len(phone_book[i]):
#             if phone_book[i].find(phone_book[j]) >= 0:
#                 return False
#             j += 1
#         i -= 1
#         j = 0
#     return True


def solution3(phone_book):
    phone_book.sort(key=len)
    phone_book.reverse()
    min_len = len(phone_book[-1])

    ht = {}
    # Create a hash table which has phone_num as key
    for phone_num in phone_book:
        ht[phone_num] = 1

    for phone_num in phone_book:
        if len(phone_num) > min_len:
            for i in range(len(phone_num)):
                for j in range(i + 1, len(phone_num)):
                    # if phone_num[i:j] in ht.keys():
                    if ht.get(phone_num[i:j]) and phone_num != phone_num[i:j]:
                        return False
    return True


def solution(phone_book):
    phone_book.sort(key=len)
    phone_book.reverse()
    min_len = len(phone_book[-1])

    ht = {}
    # Create a hash table which has phone_num as key
    for phone_num in phone_book:
        ht[phone_num] = 1
    # 1195524421
    # 1
    # 11
    # 119
    #
    # 97674223
    # 119
    test = ht.keys()
    for phone_num in phone_book:
        if len(phone_num) > min_len:
            f = len(filter(lambda key: (len(key) < len(phone_num)) and (key in phone_num), ht.keys()))
            if filter(lambda key: (len(key) < len(phone_num)) and (key in phone_num), ht.keys()):
                return False
        else:
            return True
    return True