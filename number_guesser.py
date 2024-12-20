import random

# allows the user to customise the game
min = int(input("min: "))
max = int(input("max: "))
num_of_guesses = int(input("how many guesses would you like"))


# uses a try and except block as a way to validate the user's input because if it was not a number, a value error would occur when you try and convert it into an integer
try:

    # randomly generates the number to guess using the random module
    num_to_guess = random.randint(min,max)
    attempts = 0

    while True:
        attempts += 1
        if attempts > num_of_guesses:
            print(f"you have used up all {num_of_guesses} of your guesses, the correct answer was {num_to_guess}")
            break
        try:
            guess = int(input(f"guess the number (between {min} and {max}): "))

            if guess > num_to_guess:
                print("Too high! Try again")
            elif guess < num_to_guess:
                print("Too low! Try again")
            else:
                print(f"congratulations you guessed the correct number in {attempts} attenpts")
                break
        except ValueError:
            print("enter a valid number")

except ValueError:
    print("the minimum value must be more that the maximum value")