import random
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine: "Nine", ten: "Ten", jack: "Jack", queen: "Queen", king: "King", ace: "Ace"}

player_score = 0
computer_score = 0

def start():
    print ("Let's play a game of Linux Poker.")
    while game():
        pass
    scores()

def game():
    print ("The computer will help you to pick a card.")
    cards = [nine, ten, jack, queen, king, ace]
    random.shuffle(cards)
    my_card = cards.pop()
    print ("Your card is the %s." % names[my_card])
    return play_again()