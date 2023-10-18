import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False
my_cards = []
opponent_cards = []


def sum_cards(list):
    sum = 0
    for card in list:
        sum += card
    return sum

def draw_next_card():
    my_cards.append(random.choice(cards))

def check_for_21():
    global game_over
    if sum_cards(my_cards) == 21 and sum_cards(opponent_cards) != 21:
        game_over = True
        print(f'You won!, dealer got {opponent_cards}')
    elif sum_cards(my_cards) == 21 and sum_cards(opponent_cards) == 21:
        game_over = True
        print(f"It's a draw, you both got 21")
    elif sum_cards(my_cards) > 21:
        game_over = True
        print(f"You loose! Yourr total is {sum_cards(my_cards)} and you're over 21, your cards were {my_cards}")

def check_winner():
    my_score = 21 - sum_cards(my_cards)
    opponent_score = 21 - sum_cards(opponent_cards)
    global game_over
    if abs(my_score) < abs(opponent_score):
        print(f"You won! Your cards were {my_cards} and opponent {opponent_cards}")
    elif abs(my_score) > abs(opponent_score):
        print(f"You lose! Your cards were {my_cards} and opponent {opponent_cards}")
    else:
        print(f"It's a draw! Your cards were {my_cards} and opponent {opponent_cards}")
    
    game_over = True

start = input('Would you like to start blackjack game?(y/n)\n')

if start == 'y':
    for i in range(2):
        my_cards.append(random.choice(cards))
        opponent_cards.append(random.choice(cards))

print(f"You've drawn {my_cards} and dealer drawned {opponent_cards}")

check_for_21()

while sum_cards(my_cards) < 17: 
    if sum_cards(opponent_cards) < 17:
        opponent_cards.append(random.choice(cards))

    if sum_cards(my_cards) < 17:
        input(f"You have below 17 points ({sum_cards(my_cards)}), so you must draw another card. Press ENTER key to draw another card\n")
        my_cards.append(random.choice(cards))
        check_for_21()
        print(f"Your cards {my_cards}")

while game_over != True:
    if sum_cards(my_cards) >= 17:
        #print(f"Your cards {my_cards} sum: {sum_cards(my_cards)}")
        draw_next = input("Would you like to draw next card? (y/n)?\n")
        if draw_next == 'y':
            draw_next_card()
            print(f"Your cards {my_cards} sum: {sum_cards(my_cards)}")
            check_for_21()
        else:
            check_winner()

