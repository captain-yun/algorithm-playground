from collections import deque


def solution(priorities, location):
    # answer = 0
    num_popped = 0
    priorities = deque(priorities)
    request_priority = priorities[location]

    while priorities:
        # check if there is higher priority
        if is_there_higher_priority(priorities[0], priorities):
            # yes : move it to the last position
            val = priorities.popleft()
            priorities.append(val)
            location = change_location(location, priorities)
        else:
            # no : pop it from the list and increase count
            val = priorities.popleft()
            num_popped += 1
            if is_your_request(val, request_priority, location):
                print(num_popped)
                return num_popped
            location = change_location(location, priorities)


def is_there_higher_priority(val, priorities):
    return len([x for x in priorities if x > val]) > 0


def change_location(location, priorities):
    location = location % len(priorities) - 1
    if location == -1:
        location = len(priorities) - 1
    return location

def is_your_request(val, request_priority, location):
    if val == request_priority and location == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # solution([2, 1, 3, 2], 2)
    solution([1, 1, 9, 1, 1, 1], 0)