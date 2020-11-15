# simple monty hall case with n door this checks
# the switch vs no switch scenario
from random import randint


def monty_hall(switch):
    if switch:
        print('1')
    else:
        print('2')


def generate_monty_cases(n):
    arr = []
    random_car_index = randint(0, n)
    for index in range(n):
        if index == random_car_index:
            arr.append(True)   # Car
        else:
            arr.append(False)

    return arr

