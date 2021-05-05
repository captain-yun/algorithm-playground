def solution(progresses, speeds):
    answer = []
    p = 0
    max = len(progresses) - 1

    while p <= max:
        # increase progress upon speed each day
        for i, speed in enumerate(speeds):
            progresses[i] += speed

        if progresses[p] >= 100:
            i = 1
            while p + i <= max and progresses[p + i] >= 100:
                i += 1
            if p + i > max:
                answer.append(i)
                break
            else:
                p += i
                answer.append(i)
    return answer