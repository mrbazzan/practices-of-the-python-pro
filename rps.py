import random

OPTIONS = ['rock', 'paper', 'scissors']

class RPS:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None

    def get_human(self):
        number = int(input('Enter the number of your choice: '))
        self.human_choice = OPTIONS[number - 1]

    def get_computer(self):
        self.computer_choice = random.choice(OPTIONS)

    def decider(self, lose, win):
        if self.computer_choice == lose:
            print(f'Sorry, {self.computer_choice} beat {self.human_choice}')
        elif self.human_choice == win:
            print(f'Yes, {self.human_choice} beat {self.computer_choice}')

    def print_winner(self):
        # Take care of the draw condition
        if self.human_choice == self.computer_choice:
            print("Draw")

        # Take care of win or lose
        if self.human_choice == 'paper':
            self.decider('scissors', 'rock')
        elif self.human_choice == 'rock':
            self.decider('paper', 'scissors')
        elif self.human_choice == 'scissors':
            self.decider('rock', 'paper')
        
    def main(self):
        print('(1) Rock\n(2) Paper\n(3) Scissors')

        self.get_human()
        self.get_computer()

        print(f'You chose {self.human_choice}')
        print(f'The computer chose {self.computer_choice}')

        self.print_winner()


rps = RPS()
rps.main()
