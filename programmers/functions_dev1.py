def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    # cur refers to the position where it must be completed to progress
    cur = 0
    count = 0

    # 만약 day까지 구하라고 하면
    while cur < n:
        progresses = increase(progresses, speeds)
        if progresses[cur] >= 100:
            # count how many completed
            count = count_completed(cur, progresses)
            cur += count
            answer.append(count)
            progresses = remove_completed(progresses, speeds)

    while progresses:
        progresses = increase(progresses, speeds)
        # check if there are functions completed.
        check_completed(progresses)

    return answer


def increase(list1, list2):
    return [list1[x] + list2[x] for x in range(len(list1))]

def check_completed(progresses):
    [x for x in progresses if x >= 100]

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

def remove_completed()

if __name__ == "__main__":
    solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])