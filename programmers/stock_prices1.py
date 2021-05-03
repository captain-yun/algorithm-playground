from collections import deque


def solution(prices):
    answer = []
    stack = deque()
    for i, price in enumerate(prices):
        stack = deque(prices[i+1:])
        count = 0
        # popleft() - element one by one
        # compare the price
        while stack:
            if stack.popleft() >= price:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    print(answer)
    return answer