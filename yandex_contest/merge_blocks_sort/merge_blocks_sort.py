import sys


def merge_blocks_sort(n, arr):
    block_count = 0
    max_in_block = 0
    for i in range(n):
        current_value = int(arr[i])
        if current_value > max_in_block:
            max_in_block = current_value
        if i == max_in_block:
            block_count += 1
    return block_count


if __name__ == '__main__':
    # print(merge_blocks_sort(4, [2, 1, 0, 3]))
    # print(merge_blocks_sort(8, [3, 6, 7, 4, 1, 5, 0, 2]))
    # print(merge_blocks_sort(5, [1, 0, 2, 3, 4]))
    n = sys.stdin.readline().rstrip()
    arr = sys.stdin.readline().rstrip().split()
    print(merge_blocks_sort(int(n), arr))
