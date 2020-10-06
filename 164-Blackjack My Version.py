import random
suit = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'{self.rank} of {self.suit}'
class Deck():
    def __init__(self):
        self.deck_card = []
        for s in suit:
            for r in rank:
                self.deck_card.append(Card(s,r))
    def __str__(self):
        all_card = ''
        for s in self.deck_card:
            all_card += '\n' + Card.__str__(s)
        return all_card
    def shuffle(self):
        random.shuffle(self.deck_card)
    def deal(self):
        return self.deck_card.pop(0)

class Hand():
    def __init__(self):
        self.card = []
        self.value = 0
        self.ace = 0
    def add(self,newcard):
        self.value += value[newcard.rank]
        self.card.append(newcard)
        if newcard.rank == 'Ace':
            self.ace += 1
    def checkace(self):
        if self.value > 21 and self.ace > 0:
          self.value -= 10
          self.ace -= 1
    def remove(self):
        self.card.pop(0)
class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win(self):
        self.total += self.total
        return self.total
    def lose(self):
        self.total -= self.bet
        return self.total
#Functions for the gameplay

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips do you want to bet?  '))
        except:
            print('Enter a valid value')
        else:
            if chips.bet > chips.total:
                print(f'You do not have enough chips. You have {chips.total} chips  ')
            else:
                break
def hit(deck,hand):
    hand.add(deck.deal())
    hand.checkace()

def hitorstand(deck,hand):
    global playing
    while True:
        x = input('Do you want to Hit or Stand (h/s) ?  ')
        if x[0].lower() == 'h':
            print('Player Hit')
            hit(deck,hand)
            break
        elif x[0].lower() == 's':
            print('Player Stands')
            playing = False
            break
        else:
            print('Sorry I could not understand  ')
            continue



def showsome(player,dealer):
    print('DEALER HAND')
    print('Card 1 Hidden')
    print(dealer.card[1])
    print('\n')
    print('PLAYER HAND')
    for s in player.card:
        print(s)
        
def showall(player,dealer):
    print('DEALER HAND')
    print('Card 1 Hidden\n')
    for s in dealer.card:
        print(s)
    print('\n')
    print('PLAYER HAND')
    for s in player.card:
        print(s)


def playerwins(player,dealer,chips):
    print('PLAYER WINS')
    chips.win()

def playerbust(player,dealer,chips):
    print('PLAYER BUSTS')
    chips.lose()

def dealerwins(player,dealer,chips):
    print('DEALER WINS')
    chips.lose()

def dealerbust(player,dealer,chips):
    print('DEALER BUSTS')
    chips.win()
def push(player,dealer):
    print('TIE')

#Actual Gameplay

while True:

    x = Deck()
    x.shuffle()

    p = Hand()
    p.add(x.deal())
    p.add(x.deal())

    d = Hand()
    d.add(x.deal())
    d.add(x.deal())

    c = Chips()

    take_bet(c)

    showsome(p,d)

    while playing:
        hitorstand(x,p)
        showsome(p,d)
        if p.value > 21:
            playerbust(p,d,c)
            break
        
        
    if p.value <= 21:
        while d.value < p.value:
            hit(x,d)
        showall(p,d)
        if d.value > 21:
            dealerbust(p,d,c)
        elif d.value > p.value:
            dealerwins(p,d,c)
        else:
            push(p,d)
    
    print(f'Total chips you got {c.total}')
    x = input('WOuld you like to play again? (y/n) ')
    if x[0].lower() == 'y':
        print('Player plays')
        playing = True
        continue
    elif x[0].lower() == 'n':
        print('Thank you for playing ')
    else:
        print('Please enter a valid command')
    break




















        
