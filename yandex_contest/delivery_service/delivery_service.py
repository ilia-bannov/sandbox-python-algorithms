'''
Время посылки - 18 авг 2024, 16:28:49
ID - 116950200
Ссылка на Google-документ со скриншотами заданий в Яндекс Контест -
https://docs.google.com/document/d/12Um2fb9BfmI230KYX-JJhkikFLGcU-e42jupLBXnaN8
'''

import sys


def delivery_service(data: list, limit: int) -> int:
    count = [0] * (limit + 1)
    for item in data:
        count[int(item)] += 1
    # print(count)

    left_pointer = 1
    right_pointer = len(count) - 2
    min_count = count[-1]
    count[-1] = 0

    while left_pointer < right_pointer:
        min_count += count[right_pointer]
        if right_pointer + left_pointer <= limit:
            if count[right_pointer] >= count[left_pointer]:
                count[right_pointer], count[left_pointer] = 0, 0
                left_pointer += 1
            elif count[left_pointer] > count[right_pointer]:
                count[left_pointer] -= count[right_pointer]
                count[right_pointer] = 0
        right_pointer -= 1
        if count[left_pointer] == 0:
            left_pointer += 1

    if count[left_pointer] > 0:
        if left_pointer * 2 <= limit:
            min_count += (count[left_pointer] // 2) + count[left_pointer] % 2
        else:
            min_count += count[left_pointer]
        count[left_pointer] = 0
    # print(count)
    return min_count


if __name__ == '__main__':
    # print(delivery_service([3, 1, 2, 4], int(5)))
    # print(delivery_service([1, 2], int(3)))
    # print(delivery_service([3, 2, 2, 1], int(3)))
    # print(delivery_service([3, 5, 3, 4, 1, 1, 1, 3, 3], int(5)))
    # print(delivery_service([30, 40, 40, 50, 50, 60, 70, 75, 80, 90], int(120)))
    # print(delivery_service([30, 50, 70, 80], int(100)))
    input_data = sys.stdin.readline().rstrip().split()
    limit = sys.stdin.readline().rstrip()
    print(delivery_service(input_data, int(limit)))
