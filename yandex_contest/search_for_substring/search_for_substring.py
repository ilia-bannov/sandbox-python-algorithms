import sys


def search_for_substring(data):
    unique_seq = set()
    left_index = 0
    right_index = 0
    max_count = 0
    data_len = len(data)

    while left_index < data_len and right_index < data_len:
        if data[right_index] not in unique_seq:
            unique_seq.add(data[right_index])
            right_index += 1

            max_count = len(unique_seq) if max_count < len(unique_seq) else max_count
        else:
            unique_seq.remove(data[left_index])
            left_index += 1
    # print(unique_seq)
    return max_count


if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip()
    print(search_for_substring(input_data))
