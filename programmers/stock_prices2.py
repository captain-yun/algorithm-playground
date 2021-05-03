from collections import deque


def solution(prices):
    answer = []
    stack = deque()
    for i, price in enumerate(prices):
        count = 0
        if i + 1 < len(prices):
            stack.append(prices[i + 1])
        # popleft() - element one by one
        # compare the price
        while stack:
            if stack.popleft() >= price:
                count += 1
                if i+count+1 < len(prices):
                    stack.append(prices[i+1+count])
            else:
                count += 1
                break
        answer.append(count)
    print(answer)
    return answer


if __name__ == "__main__":
    solution([1, 2, 3, 2, 3])