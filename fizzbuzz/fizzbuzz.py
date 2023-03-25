def fizzbuzz(arg: int):
    if is_fizzbuzz(arg):
        return "fizzbuzz"
    elif is_fizz(arg):
        return "fizz"
    elif is_buzz(arg):
        return "buzz"
    return arg


def is_fizzbuzz(arg: int):
    return is_fizz(arg) and is_buzz(arg)


def is_fizz(arg: int):
    return arg % 3 == 0


def is_buzz(arg: int):
    return arg % 5 == 0
