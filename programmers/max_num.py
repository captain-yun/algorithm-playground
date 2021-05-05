# def solution(numbers):
#     answer = ''
#     # Converting every element into 3 digits numbers
#     # -> Tuple or 2 dimension arrays.
#     # p_numbers = [[original number, 3digits number]...]
#     p_numbers = []
#     for number in numbers:
#         if number == 1000:
#             p_numbers.append([number, 1000])
#         elif number == 0:
#             p_numbers.append([number, 0])
#         elif number < 10:  # 1digit number should be always ahead of others
#             p_numbers.append([number, number * 1111])
#         elif number < 100:
#             p_numbers.append([number, number * 100 + (number // 10) * 10 + (number % 10)])
#         else:
#             p_numbers.append([number, number * 10 + number // 10])
#
#     # 3030 / 303
#     # 3033
#     # 30330
#     for element in list(map(lambda x: str(x[0]), sorted(p_numbers, key=lambda x: x[1], reverse=True))):
#         answer += element
#     print(answer)
#     return answer


def solution(numbers):
    answer = ''
    numbers_sorted_by_first_digit = []
    numbers_sorted_by_second_digit = []
    numbers_sorted_by_third_digit = []

    for first_digit in range(9, -1, -1):
        # filter numbers whose first digit is "i"
        for num in numbers:
            if str(num)[0] == str(first_digit):
                numbers_sorted_by_first_digit.append(num)

        for num in numbers_sorted_by_first_digit:
            # if num is one length num, attach it to the answer.
            if num < 10:
                answer += str(num)
                numbers_sorted_by_first_digit.remove(num)

        for second_digit in range(9, -1, -1):
            # 91,92,93,95,97,977,978,979
            for num in numbers_sorted_by_first_digit:
                if str(num)[1] == second_digit:
                    numbers_sorted_by_first_digit.remove(num)
                    # 97, 977, 978, 979
                    numbers_sorted_by_second_digit.append(num)

            for num in numbers_sorted_by_second_digit:
                # 1) choose the numbers whose 3-digits is upper i.
                # #97, 977, 978, 979
                if str > 100 and str(num)[2] >= second_digit:
                    numbers_sorted_by_second_digit.remove(num)
                    numbers_sorted_by_third_digit.append(num)

            # 3번째 자리로까지 정렬된 애들이 있다면 그 애들을 내림차순 정렬한다.
            if numbers_sorted_by_third_digit:
                sorted(numbers_sorted_by_third_digit, reversed=True)

            # 3자리 숫자 answer에 넣는다.
            for num in numbers_sorted_by_third_digit:
                answer += str(num)
                numbers_sorted_by_third_digit.remove(num)

            # 2자리 숫자 answer에 넣는다.
            for num in numbers_sorted_by_second_digit:
                answer += str(num)
                numbers_sorted_by_second_digit.remove(num)

    return answer
