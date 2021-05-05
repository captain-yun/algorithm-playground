from collections import deque


def solution(priorities, location):
    answer = 0

    while True:
        j = priorities.pop(0)
        if priorities and j < max(priorities):
            priorities.append(j)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            answer += 1
            if location == 0:
                return answer
            location -= 1