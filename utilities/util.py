def isZero(num: int or float) -> bool:
    return num == 0


def isPositive(num: int or float) -> bool:
    return num > 0 and not isZero(num)


def isNegative(num: int or float) -> bool:
    return num < 0 and not isZero(num)
