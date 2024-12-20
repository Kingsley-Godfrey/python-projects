import random

valid_answers = ["y", "n"]

#initialising the variables that will be used to output data about the user's session on the game
num_of_rolls = 0
num_of_individual_dice_rolled = 0

while True:

    roll_dice = str(input("Roll the dice? (y/n) "))

    if roll_dice not in valid_answers:
        print("Invalid choice!")
    else:
        if roll_dice.lower() == valid_answers[0]:
            num_of_rolls += 1
            num_of_dice = int(input("how many dice would you like to roll "))
            results = []
            for i in range(num_of_dice):
                results.append(random.randint(1,6))
            print(results)
            num_of_individual_dice_rolled += num_of_dice
        elif roll_dice.lower() == valid_answers[1]:
            print("Thanks for playing")
            print(f"you have rolled the dice {num_of_rolls} time(s) and in total you have rolled {num_of_individual_dice_rolled} dice")
            break