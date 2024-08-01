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
player_values=[]
dealer_values=[] 
print(deck)
