import sys


def is_correct_bracket_seq(brackets):
    if brackets == '':
        return True
    if len(brackets) % 2 != 0:
        return False
    index = 0
    correct_brackets_seq = ''
    open_brackets = ''
    while index < len(brackets):
        # print(f'{brackets[index]} {index}')
        if brackets[index] in '([{':
            open_brackets += brackets[index]
            correct_brackets_seq += brackets[index]
            index += 1
        else:
            if open_brackets == '':
                return False
            close_brackets = open_brackets[-1].replace('(', ')').replace('[', ']').replace('{', '}')
            correct_brackets_seq += close_brackets
            open_brackets = open_brackets[:-1]
            # index = len(correct_brackets_seq)
            index += 1
            # print(correct_brackets_seq)
    # print(correct_brackets_seq)

    if correct_brackets_seq == brackets:
        return True
    else:
        return False


if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip()
    # input_data = '(({})({[]}[])'
    print(is_correct_bracket_seq(input_data))
