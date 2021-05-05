#Q. 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라
# input : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# output : 6

# Max 높이부터 하나씩 빼서 해당 높이의 비의 양을 구한다. until 높이가 0이 될때까지
    # 범위 지정 후 비의 양 구하기

def trapping_rain_water(heights: list):
    water = 0

    while heights:
        # get those index:
        max_list = [[i, height] for i, height in enumerate(heights) if height == max(heights)]

        max_list.sort()
        if len(max_list) > 1:
            water += max_list[len(max_list)-1][0] - max_list[0][0] - len(max_list) + 1

        # remove those elements from the list
        for x in max_list:
            heights.remove(x[1])
    print(water)
    return

if __name__ == "__main__":
    trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])