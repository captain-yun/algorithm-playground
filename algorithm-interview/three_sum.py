# input : [-1, 0, 1, 2, -1, -4]

def three_sum(l: list):
    answer = []
    l.sort()
    # declare pointers
    # left, right = 0, len(l) - 1
    for i in range(len(l)):
        left, right = 0, len(l) - 1
        while left < right:
            sum_of_three = l[i] + l[left] + l[right]
            if sum_of_three < 0:
                left += 1
            elif sum_of_three > 0:
                right -= 1
            elif sum_of_three == 0:
                answer.append([l[i], l[left], l[right]])
                break
    answer = set(map(lambda x : (x[0], x[1], x[2]), answer))
    print(answer)

#

if __name__ == "__main__":
    three_sum([-4, -2, -1, -1, 0, 1, 2])
