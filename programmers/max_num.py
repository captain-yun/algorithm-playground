def solution(numbers):
    answer = ''
    # Converting every element into 3 digits numbers
    # -> Tuple or 2 dimension arrays.
    # p_numbers = [[original number, 3digits number]...]
    p_numbers = []
    for number in numbers:
        if number == 1000:
            p_numbers.append([number, 1000])
        elif number == 0:
            p_numbers.append([number, 0])
        elif number < 10:  # 1digit number should be always ahead of others
            p_numbers.append([number, number * 1111])
        elif number < 100:
            p_numbers.append([number, number * 100 + (number // 10) * 10 + (number % 10)])
        else:
            p_numbers.append([number, number * 10 + number // 10])

    # 3030 / 303
    # 3033
    # 30330
    for element in list(map(lambda x: str(x[0]), sorted(p_numbers, key=lambda x: x[1], reverse=True))):
        answer += element
    print(answer)
    return answer


if __name__ == "__main__":
    solution([3, 30, 34, 5, 9, 99, 989, 987, 1, 1000, 0])