# simple monty hall case with n door this checks
# the switch vs no switch scenario
from random import randint


class MontyHALL:
    monty_doors = []
    monty_reveal_data = {}
    player_chosen_door = None
    car_door_index = None
    number_doors = 0
    success = 0
    experiment_number = 0

    def __init__(self, number_doors):
        self.number_doors = number_doors

    def start(self, switch, times):
        # start the program here
        self.generate_monty_cases()
        self.player_chose()


        # end of the experiment reveal data
        self.print_experiment_details()

    def player_chose(self):
        self.player_chosen_door = randint(0, self.number_doors)

    def generate_monty_cases(self):
        self.car_door_index = randint(0, self.number_doors)
        for index in range(self.number_doors):
            if index == self.car_door_index:
                self.monty_doors.append(True)  # Car
            else:
                self.monty_doors.append(False)

    def monty_reveals_details_switch(self, switch):
        # assuming th monty reveals the door since we have to intention of finding out
        if self.player_chosen_door == self.player_chosen_door:
            if not switch:  # he is already under the right door
                self.success = self.success + 1
        else:
            if switch:
                self.success = self.success + 1

    def print_experiment_details(self):
        print("s", self)

    def print_monty_doors(self):
        print(self.monty_doors)

    def print_player_chosen_door(self):
        print(self.player_chosen_door)
