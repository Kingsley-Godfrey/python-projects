emojis = { 'r' : '🪨', 'p' : '📝', 's' : '✂️'}

valid_choices = tuple(emojis.keys())
winning_scenarios = ('s', 'r', 'p')

like_to_continue = 'y'

def determine_winner(choice, computer_choice):
    if valid_choices.index(choice) == winning_scenarios.index(computer_choice):
        return_results(choice, computer_choice, "won")

    elif choice == computer_choice:
        return_results(choice, computer_choice, "need a rematch")

    else:
        return_results(choice, computer_choice, "lost")


def return_results(choice, computer_choice, outcome):
    print(f'you chose {emojis[choice]}')
    print(f'the computer chose {emojis[computer_choice]}')
    print(f'you {outcome}')
    