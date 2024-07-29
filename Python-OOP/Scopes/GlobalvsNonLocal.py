x = 1


def print_global():
    print(x)


print_global()  # 1


def modify_global():
    try:
        print(x)
        x = x + 1
    except UnboundLocalError:
        print("UnboundLocalError: local variable 'x' referenced before assignment")


modify_global()  # UnboundLocalError: local variable 'x' referenced before assignment, line 8


def global_func():
    global x
    print(x)
    x = x + 1


global_func()  # 1
global_func()  # 2
global_func()  # 3


def func():
    x = 1

    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


def nonlocal_func():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


func()  # inner: 2
# outer: 1

nonlocal_func()  # inner: 2
# outer: 2
