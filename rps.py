import random

OPTIONS = ['rock', 'paper', 'scissors']

def decider(win, lose):
    if win == 'paper' and lose != 'scissors':
        return f'Yes, {win} beat {lose}'
    elif win == 'scissors' and lose != 'rock':
        return f'Yes, {win} beat {lose}'
    elif win == 'rock' and lose != 'paper':
        return f'Yes, {win} beat {lose}'

def print_winner(human_choice, computer_choice):
    if human_choice == computer_choice:
        return "Draw"
    
    winner = decider(human_choice, computer_choice)
    return (
        winner if winner
        else f'Sorry, {computer_choice} beat {human_choice}'
    )

def get_human():
    return OPTIONS[int(input('Enter the number of your choice: ')) - 1]

def get_computer():
    return random.choice(OPTIONS)

def main():
    print('(1) Rock\n(2) Paper\n(3) Scissors')

    human_choice = get_human()
    print(f'You chose {human_choice}')

    computer_choice = get_computer()
    print(f'The computer chose {computer_choice}')

    print(print_winner(human_choice, computer_choice))


main()