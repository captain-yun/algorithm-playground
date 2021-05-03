import math

def solution(answers):
    n = len(answers)
    student1 = [1, 2, 3, 4, 5] * math.ceil(n / 5)
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(n / 8)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(n / 10)
    count = [0, 0, 0]
    for i in range(n):
        if student1[i] == answers[i]:
            count[0] += 1
        if student2[i] == answers[i]:
            count[1] += 1
        if student3[i] == answers[i]:
            count[2] += 1

    answer = []
    answer = [i+1 for i, e in enumerate(count) if e == max(count)]
    answer.sort()
    print(answer)
    return answer


if __name__ == "__main__":
    solution([1,2,3,4,5])