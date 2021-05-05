def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    cur = 0
    count = 0

    while cur < n:
        progresses = increase(progresses, speeds)
        if progresses[cur] >= 100:
            # count how many completed
            count = count_completed(cur, progresses)
            cur += count
            answer.append(count)

    return answer


def increase(list1, list2):
    return [list1[x] + list2[x] for x in range(len(list1))]


def count_completed(cur, progresses):
    count = 0
    can_move = True
    while can_move and cur+count <= len(progresses)-1:
        if progresses[cur+count] >= 100:
            count += 1
            can_move = True
        else:
            can_move = False
    return count