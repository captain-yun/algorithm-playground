from collections import deque


def solution(prices):
    answer = []
    seq_prices = []

    for i, price in enumerate(prices):
        seq_prices.append([i, price])

    for seq_price in seq_prices:
        answer.append(how_long_until_down(seq_price[0], seq_price[1], prices))

    return answer


def how_long_until_down(index, price, prices):
    count = 0
    for p in prices[index + 1:]:
        count += 1
        if p < price:
            return count
    return len(prices) - index - 1