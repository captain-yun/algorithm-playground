
def array_partition_i(l:list):
    max_min_sum = 0
    while len(l) >= 2:
        num1 = max(l)
        l.remove(num1)
        num2 = max(l)
        l.remove(num2)

        max_min_sum += min(num1, num2)

    print(max_min_sum)
    return max_min_sum

def array_pair_sum_02(nums: list):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        #짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n
    return sum

def array_pair_sum_03(nums: list):
    return sum(sorted(nums)[::2])


if __name__ == "__main__":
    array_partition_i([1,4,3,2])