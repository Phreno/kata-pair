def fizzbuzz(arg: int):
    if (is_fizz(arg)):
        return "fizz"
    if (is_buzz(arg)):
        return "buzz"
    return arg


def is_fizz(arg: int):
    return arg % 3 == 0


def is_buzz(arg: int):
    return arg % 5 == 0
