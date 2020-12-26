def factorial(number: int) -> int:
    factorial_value = 1
    if number < 0:
        raise ValueError('the parameter can not be negative')

    if number == 0 or number == 1:
        return factorial_value

    for i in range(1, number + 1):
        factorial_value = factorial_value * i

    return factorial_value


def combination_length(from_element: int, chose_element: int) -> int:
    return 'ss'
