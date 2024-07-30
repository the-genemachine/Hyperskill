print("It is common to use None as a default value for optional arguments in functions.")


def say_hello(name=None):
    if name is None:
        print('Hello!')
    else:
        print(f'Hello, {name}!')


say_hello()  # 'Hello!'
say_hello('Nick')  # 'Hello, Nick!'
