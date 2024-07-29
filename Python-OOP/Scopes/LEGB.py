x = "global"


def outer():
    x = "outer local"

    def inner():
        x = "inner local"

        def func():
            x = "func local"
            print(x)

        func()

    inner()


outer()  # "func local"

x = "global"


def outer():
    x = "outer local"

    def inner():
        x = "inner local"

        def func():
            print(x)

        func()

    inner()


outer()  # "inner local"

x = "global"


def outer():
    def inner():
        def func():
            print(x)

        func()

    inner()


outer()  # "global"
