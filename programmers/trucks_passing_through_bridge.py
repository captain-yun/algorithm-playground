from collections import deque
from functools import reduce


def solution(bridge_length, weight, truck_weights):
    answer = 1

    n = len(truck_weights)
    num_of_completed = 0
    weight_in_bridge = deque()
    trucks_in_bridge = deque()
    while not num_of_completed == n:
        # 1. Check if new truck start to pass through the bridge
        if truck_weights and weight - sum_weight_in_bridge(weight_in_bridge) >= truck_weights[0]:
            trucks_in_bridge.append(bridge_length)
            weight_in_bridge.append(truck_weights[0])
            truck_weights.remove(truck_weights[0])
        # 2. 1s move
        answer += 1
        # trucks_in_bridge = list(map(lambda x: x[0]-1, trucks_in_bridge))
        # trucks_in_bridge = deque(map(lambda x: x-1, trucks_in_bridge))
        move_trucks_1s(trucks_in_bridge)

        # 3. check the changes
        # if there is truck to exit, check & remove it from trucks_in_bridge
        if trucks_in_bridge[0] == 0:
            trucks_in_bridge.popleft()
            weight_in_bridge.popleft()
            num_of_completed += 1
    print(answer)
    return answer

def sum_weight_in_bridge(weights):
    sum = 0
    for weight in weights:
        sum += weight
    return sum

def move_trucks_1s(trucks):
    for i in range(len(trucks)):
        trucks[i] -= 1

if __name__ == "__main__":
    # solution(2, 10, [7,4,5,6])
    solution(100, 100, [10,10,10,10,10,10,10,10,10,10])