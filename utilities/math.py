from utilities.util import isNegative
from utilities.util import isZero


def factorial(number: int) -> int:
    factorial_value = 1
    if isNegative(number):
        raise ValueError('the parameter can not be negative')

    if isZero(number) or number == 1:
        return factorial_value

    for i in range(1, number + 1):
        factorial_value = factorial_value * i

    return factorial_value


def factorial_R(number: int) -> int:
    if isNegative(number):
        raise ValueError('the parameter can not be negative')
    if number == 0 or number == 1:
        return 1

    return number * factorial_R(number - 1)


def combination(from_element: int, chose_element: int) -> float:
    if chose_element > from_element or isNegative(chose_element):
        return 0
    if from_element == chose_element or chose_element == 0:  # shortcut
        return 1
    if chose_element == 1:
        return from_element

    return factorial(from_element) // (factorial(from_element - chose_element) * factorial(chose_element))


def isProb(num: float or int) -> bool:
    if not isinstance(num, float) and num != 0 and num != 1:
        return False

    return 0 <= num <= 1


def nProb(num: float or int) -> float or int:
    if not isProb(num):
        raise ValueError('Invalid Format')

    return 1 - num
