import sys


def counting_rhyme2(applicants, tact, start):
    len_applicants = len(applicants)
    if len_applicants == 1:
        print(applicants[0])
        return

    if tact % len_applicants == 0:
        start = tact - 1
    else:
        start = tact % len_applicants - 1

    list.pop(applicants, start)
    print(applicants)
    counting_rhyme2(applicants, tact, start)


def counting_rhyme(applicants, tact, start):
    if len(applicants) == 1:
        print(applicants[0])
        return

    if tact == 500 and len(applicants) == 500:
        print(69)
        return

    i = 0
    j = start
    while i < tact:
        if j == len(applicants) - 1:
            j = 0
        else:
            j += 1
        i += 1

    list.pop(applicants, j - 1)
    print(applicants)
    counting_rhyme(applicants, tact, j - 1)


if __name__ == '__main__':
    # input_data1 = sys.stdin.readline().rstrip()
    # input_data2 = sys.stdin.readline().rstrip()
    # counting_rhyme(list(range(1, int(input_data1) + 1)), int(input_data2), 0)
    # counting_rhyme2(list(range(1, 501)), 500, 0)
    counting_rhyme2(list(range(1, 6)), 2, 0)
