import sys


def barometr_fibonacci(search_generation, generation=0, number1=0, number2=0):
    if generation == 0:
        number1 = 1
        number2 = 0
    if generation == 1:
        number1 = 0
        number2 = 1
    number3 = number1 + number2
    # print(f'{search_generation} {generation} : {number1} + {number2}')
    if generation == search_generation:
        print(number3)
        return
    barometr_fibonacci(search_generation, generation + 1, number2, number3)


if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip()
    barometr_fibonacci(int(input_data))
    # barometr_fibonacci(3)
