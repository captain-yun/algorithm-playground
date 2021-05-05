from functools import reduce

# def solution(citations):
#     answer = 0
#     citations.sort()
#     n = len(citations)
#     # size
#     # 1. 우선 정렬한다
#     # 2. 정렬된 원소 중 하나씩 타겟으로 하여 다음을 반복한다.
#         # 2-1. target = 1 ~ 10000
#
#     # size.sort()
#     h = 0
#     for h in range(n):
#         if len(list(filter(lambda x: x >= h, citations))) >= h and len(list(filter(lambda x: x <= h, citations))) <= h:
#             if answer <= h:
#                 answer = h
#     print(answer)
#     if citations[0] >= n:
#         answer = n
#     return answer
#


def solution(citations):
    answer = 0

    h_indexes = list(set(citations))
    h_indexes.sort()
    h_indexes.reverse()

    for h in h_indexes:
        # if len(list(filter(lambda x: x >= h, citations))) >= h and reduce(lambda x, y: x+y, (list(filter(lambda x: x < h, citations)))) <= h:
        # Using list comprehension
        if len([x for x in citations if x >= h]) >= h and reduce(lambda x, y: x + y,
                                                                 [x for x in citations if x < h]) <= h:
            return h

    return answer