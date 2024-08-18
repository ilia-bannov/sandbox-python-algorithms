import sys


def remove_duplicates():
    elements_count = int(sys.stdin.readline().rstrip())
    input_data = sys.stdin.readline().rstrip().split()
    output_data = [None] * elements_count
    prev_element = -1
    index = 0
    for element in input_data:
        if element != prev_element:
            output_data[index] = element
            prev_element = element
            index += 1

    while index < elements_count:
        output_data[index] = '_'
        index += 1

    print(' '.join(output_data))


if __name__ == '__main__':
    remove_duplicates()
