# simple monty hall case with n door this checks
# the switch vs no switch scenario
from random import randint


class MontyHALL:
    # constant through whole object cycle
    number_doors = 0
    success = 0
    experiment_number = 0

    # changed with every go
    # number from 0 -> n
    # monty_chosen_door = None
    player_chosen_door = None
    car_door_index = None

    def __init__(self, number_doors):
        self.number_doors = number_doors

    def re_initialize(self):
        self.player_chosen_door = None
        self.car_door_index = None

    def start(self, switch, times=1, single_experiment_detail=False):
        # start the program here
        self.experiment_number = times
        experiment_times_local = times

        while experiment_times_local:
            self.re_initialize()
            self.car_chosen()
            self.player_chose()
            self.monty_reveals_details_switch(switch)
            experiment_times_local = experiment_times_local - 1
            if single_experiment_detail:
                self.print_experiment_details()

        # end of the experiment reveal data
        # self.print_results(switch)

    def player_chose(self):
        self.player_chosen_door = randint(0, self.number_doors - 1)

    def car_chosen(self):
        self.car_door_index = randint(0, self.number_doors - 1)

    def monty_reveals_details_switch(self, switch):
        # assuming th monty reveals the door since we have to intention of finding out
        if self.car_door_index == self.player_chosen_door:
            if not switch:  # he is already under the right door
                self.success = self.success + 1
        else:
            if switch:  # he had chosen the wrong door at first but did switch
                self.success = self.success + 1

    def print_experiment_details(self):
        # singular run detail
        # self.print_monty_doors()
        self.print_player_chosen_door()
        self.print_car_position()

    def print_results(self, switch):
        print("/**************************************************************/")
        print("Strategy Switch: ", switch)
        print("Success: ", self.success)
        print("Losses: ", self.experiment_number - self.success)
        print("Total: ", self.experiment_number)
        print("Ratio: ", self.success / self.experiment_number)
        print("/**************************************************************/")

    def print_player_chosen_door(self):
        print("Player has Chosen: ", self.player_chosen_door)

    def print_car_position(self):
        print("Car is at :", self.car_door_index)


ob = MontyHALL(3)
ob.start(True, 2, True)
