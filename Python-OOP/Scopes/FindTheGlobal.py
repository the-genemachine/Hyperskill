a = 1
b = 2


def func():
    c = 3
    d = a + b
    global e
    e = b + c
    f = 4

    def inner_func():
        nonlocal f
        f = 5

    inner_func()


func()
