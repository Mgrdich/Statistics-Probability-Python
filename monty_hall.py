# simple monty hall case with n door this checks
# the switch vs no switch scenario
from random import randint


class MontyHALL:
    monty_doors = []
    player_chosen_door = False  # undefined
    number_doors = 0
    car_door_index = False  # undefined

    def __init__(self, number_doors):
        self.number_doors = number_doors

    def player_chose(self):
        self.player_chosen_door = randint(0, self.number_doors)

    def generate_monty_cases(self):
        self.car_door_index = randint(0, self.number_doors)
        for index in range(self.number_doors):
            if index == self.car_door_index:
                self.monty_doors.append(True)  # Car
            else:
                self.monty_doors.append(False)

    def monty_reveals_details(self):
        if self.player_chosen_door == self.player_chosen_door:
            print('player already have the right door')
        else:
            print('car is on some other door')

    def print_monty_doors(self):
        print(self.monty_doors)

    def print_player_chosen_door(self):
        print(self.player_chosen_door)
