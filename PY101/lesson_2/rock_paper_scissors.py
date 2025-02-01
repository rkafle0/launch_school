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

def get_player_choice():
    message = ', '.join(
            f'{key} ({name})' for key, name in VALID_CHOICES.items()
    )

    while True:
        prompt(f'Choose one: {message}')
        choice = input().lower()
        if choice in VALID_CHOICES:
            return choice
        prompt("That is not a valid choice.")

def display_round_result(winner):
    if winner == 1:
        prompt('Player wins!')
    elif winner == -1:
        prompt('Computer wins!')
    else:
        prompt('It is a tie!')

def adjust_scores(winner_outcome, current_scores):
    if winner_outcome == 1:
        current_scores["player"] += 1
    elif winner_outcome == -1:
        current_scores["computer"] += 1

    prompt(f'Player: {current_scores["player"]}'
            f'- Computer: {current_scores["computer"]}')

def is_match_won(current_scores):
    return current_scores["player"] == 3 or current_scores["computer"] == 3

def display_match_winner(current_scores):
    if current_scores["player"] == 3:
        prompt('We have a winner! Player wins.')
    else:
        prompt('We have a winner! Computer wins.')

def play_again():
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer in ['y']:
            return True
        if answer in ['n']:
            return False

        prompt("Please enter in 'y' or 'n'.")

scores = {'player': 0, 'computer': 0}

while True:
    player_choice = get_player_choice()
    comp_choice = random.choice(list(VALID_CHOICES.keys()))
    winner_result = compute_winner(player_choice, comp_choice)

    prompt(f'Player chose: {VALID_CHOICES[player_choice]}. '
            f'Computer chose: {VALID_CHOICES[comp_choice]}.')

    display_round_result(winner_result)
    adjust_scores(winner_result, scores)

    if is_match_won(scores):
        display_match_winner(scores)
        scores = {'player': 0, 'computer': 0}

    if not play_again():
        prompt("Thanks for playing. Goodbye!")
        break