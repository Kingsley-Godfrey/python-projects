import random
# imports the rock_paper_scissors_extension.py which contains all the data and functions needed for the program so that the main file is just the logic
import rock_paper_scissors_extension

try:
    while rock_paper_scissors_extension.like_to_continue == 'y':
        while True:
            # gets the choices of the player and the computer
            choice = input("rock, paper or scissors (r/p/s) ").lower()
            computer_choice = random.choice(rock_paper_scissors_extension.valid_choices)

            # calls the determine winner function from the other python file
            rock_paper_scissors_extension.determine_winner(choice, computer_choice)
            break
             
        rock_paper_scissors_extension.like_to_continue = input("Would you like to continue (y/n)").lower()

except ValueError:
    print("you must enter r, p or s")