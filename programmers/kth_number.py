def solution(array, commands):
    answer = []

    # commands[0] .. commands[1]로 짜로고 commands[2]를 찾아라

    for command in commands:
        count = 0
        arr = array[command[0]-1:command[1]]
        arr.sort()
        for element in arr:
            count += 1
            if count == command[2]:
                answer.append(element)
    print(answer)
    return answer


if __name__ == "__main__":
    solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])