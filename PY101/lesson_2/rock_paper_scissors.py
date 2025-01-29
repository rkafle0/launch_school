import random

VALID_CHOICES = {
    "r"  : "rock",
    "p"  : "paper",
    "s"  : "scissors",
    "sp" : "spock",
    "l"  : "lizard",
}

WINNING_CHOICES = {
    "rock"     : ["lizard", "scissors"],
    "paper"    : ["rock", "spock"],
    "scissors" : ["paper", "lizard"],
    "spock"    : ["rock", "scissors"],
    "lizard"   : ["spock", "paper"],
}

def prompt(message):
    print(f"==> {message}")

def compute_winner(player, computer):
    computer = VALID_CHOICES[computer]
    player = VALID_CHOICES[player]

    if player == computer:
        return None
    if computer not in WINNING_CHOICES[player]:
        return -1
    return 1

scores = {'player': 0, 'computer': 0}

while True:
    MESSAGE = ', '.join(
            f'{key} ({name})' for key, name in VALID_CHOICES.items()
    )

    prompt(f'Choose one: {MESSAGE}')
    choice = input().lower()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        prompt(MESSAGE)
        choice = input()

    computer_choice = random.choice(list(VALID_CHOICES.keys()))
    winner_result = compute_winner(choice, computer_choice)

    if winner_result == 1:
        prompt('Player wins!')
        scores["player"] += 1
    elif winner_result == -1:
        prompt('Computer wins!')
        scores["computer"] += 1
    else:
        prompt('It is a tie!')

    prompt(f'Player: {scores["player"]} - Computer {scores["computer"]}')

    if scores["player"] == 3:
        prompt('We have a winner! Player wins.')
        break

    if scores["computer"] == 3:
        prompt('We have a winner! Computer wins.')
        break

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("That's not a valid choice")

    if answer[0] == 'n':
        break