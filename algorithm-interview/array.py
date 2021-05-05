
def two_sum(nums: list, target: int):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    # {2:0, 5:1, 7:2, ... }

    for i, num in enumerate(nums):
        complement = target - num
        if nums_map[complement] and i != nums_map[complement]:
            return i, nums_map[complement]
