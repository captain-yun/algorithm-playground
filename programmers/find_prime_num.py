import itertools


def solution(numbers):
    primes = set()
    n = len(numbers)
    answer = 0

    for i in range(1, n+1):
        every_combinations = [''.join(i) for i in itertools.permutations(numbers, i)]
        for num in every_combinations:
            is_prime(num, primes)

    answer = len(primes)
    print(answer)
    return answer


def is_prime(num, primes):
    if int(num) <= 1:
        return 0
    # check for factor
    for i in range(2, int(num)):
        if int(num) % i == 0:
            return 0
    else:
        primes.add(int(num))
        return 1


if __name__ == "__main__":
    solution("011")
