import math

counter = 0

x=0

def f(x):
    global counter

    counter += 1
    return x + counter

print(str(f(x)+f(x)))
print(str(2*f(x)))


def f(): return 2

print(f() + f())
print(2)

def f(): return 2

print(2 + f())
print(f())
