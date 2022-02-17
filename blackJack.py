#OBJECT ORIENTED PRACTICE
#GOAL: IMPLEMENT A GAME OF BLACKJACK


class Card: 
    """
    A class used to represent a Card
    ...
    Attributes
    ----------
    suit : str
    	the suit name
    rank : str
    	the rank of a card
    value : int
    	the int value of a rank
    """
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit 



suits =('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

