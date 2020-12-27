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


def combination(from_element: int, chose_element: int) -> float:
    if from_element == chose_element or chose_element == 0:  # shortcut
        return 1
    if chose_element == 1:
        return from_element

    return factorial(from_element) / (factorial(from_element - chose_element) * factorial(chose_element))
