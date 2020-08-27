import random		#to shuffle the deck

suits = ('hearts','diamonds','spades','clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','King','Queen','Jack','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'King':10,'Queen':10,'Jack':10,'Ace':11}

playing = True		#for controlling while loops

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:		#to store the 52 card objects
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        
    
    def __str__(self):
        resultstr=''
        for x in self.deck:
            resultstr=resultstr+'\n'+x.__str__()   #important
        return resultstr

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        singlecard=self.deck.pop()      #important
        return singlecard

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value=self.value+values[card.rank]
        
        if card.rank=='Ace':
            self.aces+=1
        
    def adjust_for_ace(self):
        while self.value>21 and self.aces:		#aces can have the value 1 or 11
            self.value-=10
            self.aces-=1
class Chips:
    
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("Enter bet amount"))
        except:
            print("Input is incorrect!")
        else:
            if chips.bet>chips.total:
                print(f"you do not have enough chips. you have {chips.total} chips.")
            else:
                break

def hit(deck,hand):
    hitcard=deck.deal()
    hand.add_card(hitcard)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control the while loop
    
    while True:
        choice=input('Hit or stand?')
        if choice[0].lower()=='h':
            hit(deck,hand)
        elif choice[0].lower()=='s':
            print("Player stands. It is the dealer's chance")
            playing=False
        else:
            print("Wrong input")
            continue
        break

def show_some(player,dealer):				#each time player takes a card
    print("Dealer's hidden card: ", dealer.cards[1])
    print("Player's cards: ", *player.cards, sep='\n')
    
def show_all(player,dealer):				#at the end of the hand
    print("Dealer's cards: ", *dealer.cards, sep='\n')
    print("Dealer's value: ",dealer.value)
    print("Player's cards: ", *player.cards, sep='\n')
    print("Player's value: ",player.value)

def player_busts(player,dealer,chips):		#to handle all ending scenarios
    print("Player busts.")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins.")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts.")
    chips.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins.")
    chips.win_bet()
    
def push(player,dealer,chips):
    print("It's a tie/push.")

while True:
    print("Welcome to the game!")
    
    # we create & shuffle the deck and deal two cards to each player
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    dealer_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Player's chips
    player_chips=Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show some cards
    show_some(player_hand,dealer_hand)
    
    while playing:  #variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show some cards 
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, player busts
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, Dealer's hand is played until Dealer reaches 17
    if player_hand.value<=21:
        while dealer_hand.value<17:
            hit_or_stand(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # different ending scenarios
        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_busts(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total 
    print("Player's total chips: ", player_chips.total)
    
    # Ask to play again
    play_again=input("Do you wish to play again? type yes or no.")
    if play_again[0].lower()=='y':
        player=True
        continue
    else:
        print("Tha game has finished")
        break