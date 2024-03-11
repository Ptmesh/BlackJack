import random
from art import logo
def deal_card():
    '''Give a random card from deck!'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # It means that the particular side will hit a blackjack!
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Nahitr add the sum of the first two drawn cards..
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Comparing the score here
def compare(userScore , dealerScore):
    # Itna samajh ajayega..else go and check my flowchart!n
    if userScore == dealerScore:
        return "Draw! 😩"
    elif dealerScore == 0:
        return "Lose! , dealer has an blackjack 🥲 "
    elif userScore == 0:
        return "Win with a blackjack 🥳!!!"
    elif userScore > 21:
        return "You went over..You lose😭"
    elif dealerScore > 21:
        return "Dealer went over ,You win!👀💸"
    elif userScore > dealerScore:
        return "You Win😸"
    else:
        return "You Lose 😔"

def start_game():
    user_cards = []
    dealer_cards = []

    isGameOver = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not isGameOver:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your card:{user_cards} and score:{user_score} \nDealer's first card:{dealer_cards[0]} ")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            isGameOver = True
        else:
            user_deal = input("Type 'y' to get another card or type 'n' to pass:\n")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                isGameOver = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score += calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score:{user_score}\n")
    print(f"Dealer's final hand: {dealer_cards}, final score:{dealer_score}\n")
    print(compare(userScore=user_score , dealerScore=dealer_score))

print(logo)
while  input("Do you wanna play a game of blackjack?? Type 'y' or 'n' ").lower() == "y":

    start_game()

