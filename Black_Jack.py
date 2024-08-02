import random as r
suits=['Clubs','Diamonds','Hearts','Spades']
values={'Two':2,'Three':3,"Four":4,'Five':5,'Six':6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
orgdeck=[]
for suit in suits:
    for value in values:
        orgdeck.append(f"{value} of {suit}") 
deck=orgdeck[:]
player_hand=[] 
dealer_hand=[]
player_values=0
dealer_values=0

#Shuffle Deck
r.shuffle(deck) 

#Dealing Card to Player 
player_hand.append(deck[0]) 
player_hand.append(deck[1])
deck.pop(0)
deck.pop(1)
#Dealing Card to Dealer 
dealer_hand.append(deck[2])
dealer_hand.append(deck[3])
deck.pop(2)
deck.pop(3)


#Calculating Hand Values 
def hand_value(hand): 
    value=0 
    ace=0 
    for card in hand: 
        card=card.split()
        card_value=card[0]
        value+=values[card_value] 
        if card_value=="Ace": 
            ace+=1 
    while value>21 and ace: 
        value-=1
        ace-=1 
    return value 

#Game start 

player_name=input("Hello!, Please enter your name:")
player_bet=int(input("Enter the amount you would like to bet:"))


print(f"Hello {player_name},this is your hand {player_hand}")
print(f"Dealers hand:{dealer_hand[0]}")

#Player's turn 

playing=True 
while playing: 
    player_values=hand_value(player_hand)
    if player_values>21: 
        print("Sorry you lose!")
        break
    hitorstand=input("Enter hit if you would like to hit or stand if you would like to stand: ").lower()
    if hitorstand=="hit": 
        player_hand.append(deck[4])
        deck.pop(4) 
        player_values=hand_value(player_hand)
        print(f"Your new hand is {player_hand}")
    elif hitorstand=="stand": 
        break 
    else: 
        print("you entered the wrong value") 

#Dealers Turn 
while hand_value(dealer_hand)<=16: 
    dealer_hand.append(deck[5])
    dealer_values=hand_value(dealer_hand)
    print(f"Dealers Hand {dealer_hand}")
#Winner Calculations
if player_values>21: 
    print(f"Dealer Wins! You lost ${player_bet}!")
elif dealer_values>21 or player_values>dealer_values: 
    player_bet*=2
    print(f"Congratulations {player_name}! You win! Cashout ${player_bet}")
elif player_values<dealer_values: 
    print(f"Dealer Wins! You lost ${player_bet}!")
else: 
    print("It is a tie! No one wins!") 

print("Game over!")
close=input("Press X to close this game: ") 