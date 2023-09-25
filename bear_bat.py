from random import random


class BearBat:
    # Build a bear

    def __init__(self, name, arms, legs, body, ears, e_n_m, bat_wings):
        # Basic Build A Bear
        self.name = name
        self.arms = arms
        self.legs = legs
        self.body = int(body)
        self.e_n_m = e_n_m  # eyes nose mouth
        self.ears = ears
        self.energy = 1000

        # Adding bat wings to the bear
        self.bat_wings = bat_wings

    # Basic's for any build a bear
    def walking(self, walking=10):
        if self.legs == "long" and self.body < 5:
            self.energy -= walking
        else:
            self.energy -= walking * 2
        if self.energy < walking:
            print(f"{self.name} cannot walk. Not enough energy")
        else:
            print(f"{self.name} is walking. Energy remaining: {self.energy}")

    # bear eating its own food
    def eating(self, food):
        if food == "honey":
            self.energy += 100
        elif food == "bugs":
            self.energy += 50
        elif food == "berries":
            self.enery += 20
        else:
            print(f"{self.name} doesn't like {food}!")

    # how the bear gets its own food
    def foraging(self):
        # randomly find honey or bugs or berries
        food_options = ["honey", "bugs", "berries", "worms", "tree bark", "a fart"]
        selected_food = random.choice(food_options)
        print(f"{self.name} found {selected_food} while foraging.")
        self.eating(selected_food)
        return selected_food

    # Adding a flying method, maybe flying will make the bear better?
    # stronger?
    # I don't know?
    def flying(self, flapping=20):
        # too much stuffing and the wings might not work that well
        if self.bat_wings == "large" and self.body < 5:
            self.energy -= flapping
        else:
            self.energy -= flapping * 3

        if self.energy < flapping:
            print(f"{self.name} cannot fly. Not enough energy.")
            return False
        else:
            print(f"{self.name} is flying. Energy remaining: {self.energy}")
            return True
