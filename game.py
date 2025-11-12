print("Welcome to rock, paper, scissors")
player = input("Choose rock, paper, or scissors: ")
player = player.lower()

while True:
    if (player != "rock" and player != "paper" and player != "scissors"):
        player = input("Choose rock, paper, or scissors: ")
        player = player.lower()
    else:
        print(f"You chose: {player}.")
        break

import random

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])