import sys


def find_element(sorted_numbers, element):
    left = 0
    right = len(sorted_numbers)
    success_mid = 0
    while left < right:
        mid = (left + right) // 2
        # print(f'left = {left}, right = {right}'
        #       f'mid = {mid}, success_mid = {success_mid}')
        current_element = int(sorted_numbers[mid])
        if current_element == element:
            success_mid = mid
        if current_element < element:
            left = mid + 1
        else:
            right = mid
    return right if success_mid == 0 else success_mid


def index_determine():
    input_array = sys.stdin.readline().rstrip().split()
    input_number = int(sys.stdin.readline().rstrip())
    output_number = find_element(input_array, input_number)
    print(output_number)


if __name__ == '__main__':
    index_determine()
