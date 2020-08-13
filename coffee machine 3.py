class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.choice = ""
        self.state = 0          # State Map
                                # 0 - allow action to be selected
                                # 1 - allow purchase to be selected
                                # 2 - query refill value, water
                                # 3 - update water value (refill)
                                # 4 - query refill value, milk
                                # 5 - update milk value (refill)
                                # 6 - query refill value, coffee
                                # 7 - update coffee value (refill)
                                # 8 - query refill value, cups
                                # 9 - update cups value (refill)

    def action(self, choice):
        self.choice = choice
        if self.state == 0:
            print()
            if choice == "buy":
                self.state = 1
            elif choice == "fill":
                self.state = 2
            elif choice == "take":
                self.take()
            elif choice == "remaining":
                self.remaining()
        elif self.state == 1:
            if self.choice == "1" or self.choice == "2" or self.choice == "3":
                self.buy()
            else:
                self.state = 0
        elif self.state == 3:
            self.water += int(choice)
            self.state = 4
        elif self.state == 5:
            self.milk += int(choice)
            self.state = 6
        elif self.state == 7:
            self.coffee += int(choice)
            self.state = 8
        elif self.state == 9:
            self.cups += int(choice)
            self.state = 0

    def buy(self):
        espresso = [250, 0, 16, 1, 4]
        latte = [350, 75, 20, 1, 7]
        cappuccino = [200, 100, 12, 1, 6]
        coffee_table = [espresso, latte, cappuccino]
        fail = 0
        if self.choice == "1" or self.choice == "2" or self.choice == "3":
            selection = int(self.choice)
            if self.water < coffee_table[selection - 1][0]:
                print("Sorry, not enough water!")
                fail = 1
            else:
                self.water -= coffee_table[selection - 1][0]
            if self.milk < coffee_table[selection - 1][1]:
                print("Sorry, not enough milk!")
                fail = 1
            elif fail == 0:
                self.milk -= coffee_table[selection - 1][1]
            if self.coffee < coffee_table[selection - 1][2]:
                print("Sorry, not enough coffee!")
                fail = 1
            elif fail == 0:
                self.coffee -= coffee_table[selection - 1][2]
            if self.cups < coffee_table[selection - 1][3]:
                print("Sorry, not enough cups!")
                fail = 1
            elif fail == 0:
                self.cups -= coffee_table[selection - 1][3]
            if fail == 0:
                self.money += coffee_table[selection - 1][4]
                print("I have enough resources, making you a coffee!")
        self.state = 0
        # Any other selection is treated as "back" - sending user back to the main menu

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$" + str(self.money), "of money")


choice = ""


def action():
    global choice
    if device.state == 0:
        print()
        print("Write action (buy, fill, take, remaining, exit):")
        choice = input()
        device.action(choice)
    if device.state == 1:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()
        device.action(choice)
    if device.state == 2:
        print("Write how many ml of water do you want to add:")
        device.state += 1
        choice = input()
        device.action(choice)
    if device.state == 4:
        print("Write how many ml of milk do you want to add:")
        device.state += 1
        choice = input()
        device.action(choice)
    if device.state == 6:
        print("Write how many grams of coffee do you want to add:")
        device.state += 1
        choice = input()
        device.action(choice)
    if device.state == 8:
        print("Write how many disposable cups of coffee do you want to add:")
        device.state += 1
        choice = input()
        device.action(choice)


device = CoffeeMachine()
while choice != "exit":
    action()
