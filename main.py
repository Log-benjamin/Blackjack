import random
import os
from art import logo

deck_of_cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q']
player_score = 0
computer_score = 0

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 21:
        return "Lose, Opponent has Blackjack"
    elif user_score == 21:
        return "Win with a black jack"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You Win."
    else:
        return "You lose."

def sum_result(player):
    score = 0
    for x in player:
        if x == 'A' and score< 11:
            x = 11
        elif x == 'A' and score > 10:
            x = 1
        if x == 'J' or x == 'K' or x =='Q':
            x = 10
        score += x
    return score

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while want_to_play == "y":
    player_card = [random.choice(deck_of_cards), random.choice(deck_of_cards)]
    computer_card = [random.choice(deck_of_cards), random.choice(deck_of_cards)]
    os.system('cls')
    print(logo)
    player_score = sum_result(player_card)
    computer_score =sum_result(computer_card)

    print(f"Your cards: {player_card}, your_current_score: {player_score}")
    print(f"Computer's first card: {computer_card[0]}")

    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    while get_another_card == "y" and (player_score < 22 and computer_score < 22):
        player_card.append(random.choice(deck_of_cards))
        player_score = sum_result(player_card)
        if computer_score < 17:
            computer_card.append(random.choice(deck_of_cards))
            computer_score = sum_result(computer_card)
        
        print(f"Your cards: {player_card}, your_current_score: {player_score}")
        print(f"Computer's first card: {computer_card[0]}")
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    print(f"Your final hand: {player_card}, your_final_score: {player_score}")
    print(f"Computer's first card: {computer_card[0]}, computer_final_score: {computer_score}")
    
    print(compare(player_score, computer_score))
        
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

print("GoodBye")