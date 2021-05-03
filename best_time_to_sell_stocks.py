import sys


def max_profit(prices):
    max_price = 0

    for i, price in enumerate(prices):
        if i < len(prices) - 1 and max(prices[i+1:]) - price > max_price:
            max_price = max(prices[i+1:]) - price
    print(max_price)

# book example
def max_profit(prices):
    profit = 0
    max_price = sys.maxsize     # why we use max value? 최대값에는 가장 낮은 값을, 최소값에는 가장 높은 값을...
                                #  mx = -sys.maxsize / mn = sys.maxsize


if __name__ == "__main__":
    max_profit([7,1,5,3,6,4])