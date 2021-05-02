from functools import reduce

def multiple_except_self(nums):
    answer = []
    for i, num in enumerate(nums):
        copy_nums = []
        copy_nums = nums.copy()
        copy_nums.pop(i)
        answer.append(reduce(lambda x, y: x * y, copy_nums))
    print(answer)
    return answer


if __name__ == "__main__":
    multiple_except_self([1,2,3,4])