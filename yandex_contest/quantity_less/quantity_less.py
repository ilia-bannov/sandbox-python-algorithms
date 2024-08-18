import sys


def quantity_less(input_data):
    output_data = [None] * len(input_data)
    index = 0
    for i in input_data:
        count = 0
        for j in input_data:
            if int(i) > int(j):
                count += 1
        output_data[index] = str(count)
        index += 1

    return output_data


if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split()
    print(' '.join(quantity_less(input_data)))
