import random

def RollDice(rolls):
    for i in range(0, rolls):
        number = random.randint(1, 6)
        print()
        print([number])
        print()

def Menu() :
    choice = (0)
    while (choice != "3") :
        print("1. Roll a Die")
        print("2. Roll Multiple Dice")
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("3. Exit Program")
        choice = int(input("Enter here: "))
        print()

        if(choice == 1):
            RollDice(1)
        if(choice == 2):
            rolls = int(input("How many dice would you like to roll? "))
            RollDice(rolls)
        if(choice == 3):
            quit()

Menu()
