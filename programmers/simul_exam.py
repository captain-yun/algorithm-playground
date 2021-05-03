import math

def solution(answers):
    n = len(answers)
    student1 = [1, 2, 3, 4, 5] * math.ceil(n / 5)
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(n / 8)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(n / 10)
    count = {1 : 0, 2 : 0, 3 : 0}
    for i in range(n):
        if student1[i] == answers[i]:
            count[1] += 1
        if student2[i] == answers[i]:
            count[2] += 1
        if student3[i] == answers[i]:
            count[3] += 1

    # count = dict(filter(lambda x: x[1] > 0, count))
    # l = []
    # for student in count:
    #     l.append((student[0], student[1]))
    # l.sort(lambda x:x[1], reverse=True)
    # for student in count:
    # answers = map(x[0], l)
    return answer


if __name__ == "__main__":
    solution([3, 30, 34, 5, 9, 99, 989, 987, 1, 1000, 0])