import sys


def template_sort(n, arr, m, template):
    output_data = []
    not_in_template = list.copy(arr)
    # index = 0
    for i in template:
        for j in range(n):
            if int(arr[j]) == int(i):
                not_in_template.remove(arr[j])
                output_data.append(i)
                # index += 1

    for i in range(1, len(not_in_template)):
        current = not_in_template[i]
        prev = i - 1
        while prev >= 0 and int(not_in_template[prev]) > int(current):
            not_in_template[prev + 1] = not_in_template[prev]
            prev -= 1
        not_in_template[prev + 1] = current

    list.extend(output_data, not_in_template)
    return output_data


if __name__ == '__main__':
    n = sys.stdin.readline().rstrip()
    arr = sys.stdin.readline().rstrip().split()
    m = sys.stdin.readline().rstrip()
    template = sys.stdin.readline().rstrip().split()
    print(' '.join(template_sort(int(n), arr, int(m), template)))
    # print(template_sort(10, [2, 4, 3, 5, 6, 0, 9, 8, 7, 7], 6, [2, 4, 3, 5, 6, 0]))
    # print(template_sort(11, [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], 6, [2, 1, 4, 3, 9, 6]))
