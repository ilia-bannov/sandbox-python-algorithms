import sys


def valid_mountain_array(mountain_aray):
    array_len = len(mountain_aray)
    peak = int(mountain_aray[1])

    if array_len < 3:
        return False

    peak = 0
    prev_element = int(mountain_aray[0])
    for index in range(1, array_len):
        element = int(mountain_aray[index])
        if element > prev_element:
            peak = element
            prev_element = element
        else:
            break

    if peak == 0:
        return False

    valid = True
    prev_element = peak
    for right_index in range(index, array_len):
        element = int(mountain_aray[right_index])
        if element < prev_element:
            prev_element = element
        else:
            valid = False
            break

    return valid


if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split()
    print(valid_mountain_array(input_data))
