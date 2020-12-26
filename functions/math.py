def factorial(number: int) -> int:
    factorial_value = 1
    if number < 0:
        raise ValueError('the parameter can not be negative')

    if number == 0 or number == 1:
        return factorial_value

    for i in range(1, number + 1):
        factorial_value = factorial_value * i

    return factorial_value


def factorial_recursive(number: int) -> int:
    if number < 0:
        raise ValueError('the parameter can not be negative')
    if number == 0 or number == 1:
        return 1

    return number * factorial_recursive(number - 1)


def combination_length(from_element: int, chose_element: int) -> int:
    return 1
