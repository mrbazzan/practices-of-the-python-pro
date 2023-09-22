import random

OPTIONS = ['rock', 'paper', 'scissors']

def decider(human_choice, computer_choice, lose, win):
    if computer_choice == lose:
        print(f'Sorry, {computer_choice} beat {human_choice}')
    elif human_choice == win:
        print(f'Yes, {human_choice} beat {computer_choice}')

def print_winner(human_choice, computer_choice):
    # Take care of the draw condition
    if human_choice == computer_choice:
        print("Draw")

    # Take care of win or lose
    if human_choice == 'paper':
        decider(human_choice, computer_choice, 'scissors', 'rock')
    elif human_choice == 'rock':
        decider(human_choice, computer_choice, 'paper', 'scissors')
    elif human_choice == 'scissors':
        decider(human_choice, computer_choice, 'rock', 'paper')

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

    print_winner(human_choice, computer_choice)


main()