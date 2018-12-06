# -*- utf-8 -*-

foo = 0

def show():
    print(foo)


def fib_yield(n):
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a+b

def fib(n):
    for num in fib_yield(n):
        print(num)
# write
# write