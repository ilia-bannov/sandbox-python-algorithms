import inspect
import sys
import time


def print_call_stack():
    """Функция распечатки имён функций в стеке."""
    print([frame.function for frame in inspect.stack()])


def fib_recursion(n):
    # print_call_stack()
    if n <= 1:
        return n
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    n = 35
    start_time = time.time()
    print(fib_iterative(n))
    print('Iterative solution time:', time.time() - start_time)
    print(sys.getrecursionlimit())
    # print_call_stack()
    start_time = time.time()
    print(fib_recursion(n))
    print('Recursive solution time:', time.time() - start_time)
    # print_call_stack()
