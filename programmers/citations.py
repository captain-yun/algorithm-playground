from functools import reduce

def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    # size
    # 1. 우선 정렬한다
    # 2. 정렬된 원소 중 하나씩 타겟으로 하여 다음을 반복한다.
        # 2-1. target = 1 ~ 10000

    # size.sort()
    h = 0
    for h in range(n):
        if len(list(filter(lambda x: x >= h, citations))) >= h and len(list(filter(lambda x: x <= h, citations))) <= h:
            if answer <= h:
                answer = h
    print(answer)
    if citations[0] >= n:
        answer = n
    return answer


if __name__ == "__main__":
    solution([3, 0, 6, 1, 5])