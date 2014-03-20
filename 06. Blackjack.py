# Mini-project #6 - Blackjack -simplified
#
# 'Introduction to Interactive Programming in Python' Course
# RICE University - coursera.org
# by Joe Warren, John Greiner, Stephen Wong, Scott Rixner
# run the code using www.codesculptor.org


# link to code http://www.codeskulptor.org/#user28_aubOa4HNZ1_18.py


import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        pass	# create Hand object

    def __str__(self):
        CARDS = ""
        for card in self.hand:
            CARDS += str(card) +" "
        return "Hand contains " + CARDS
        pass	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)
            # add a card object to a hand

    def get_value(self):
        hand_value = 0
        ace_inhand = False
        for card in self.hand:
            if card.get_rank() == 'A':
                ace_inhand = True
            hand_value += VALUES[card.get_rank()]
        if (ace_inhand == True) and (hand_value + 10 < 22):
            return hand_value + 10
        else:
            return hand_value
   
    def draw(self, canvas, pos):
        for card in self.hand:
            pos[0] += CARD_SIZE[0] + 20
            card.draw(canvas, pos)
        
       
        pass	# draw a hand on the canvas, use the draw method for cards
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,  rank))
 
    # shuffle the deck 
    def shuffle(self):
        random.shuffle(self.deck)
        
    # deal a card object from the deck
    def deal_card(self):
        return self.deck.pop()
 
    # return a string representing the deck
    def __str__(self):
        CARDS = ""
        for card in self.deck:
            CARDS += str(card) +" "
        return "Deck contains " + CARDS
        

#define event handlers for buttons
def deal():
    global outcome, in_play, message, dealer_hand, player_hand, deck, score
    if in_play:
        score -= 1
        in_play = False
        deal()
    else:
        outcome = ""
        message = "Hit or Stand?"
        deck = Deck()
        deck.shuffle()
        dealer_hand = Hand()
        player_hand = Hand()
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        in_play = True

        
def hit():
    global outcome, in_play, message, dealer_hand, player_hand, deck, score
    if in_play:
        if player_hand.get_value() < 22:
            player_hand.add_card(deck.deal_card())
            if player_hand.get_value() > 21:
                outcome = "Player bust and loses"
                score -= 1
                message = "New game?"
                in_play = False
            
       
def stand():
    global outcome, in_play, message, dealer_hand, player_hand, deck, score
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() == player_hand.get_value():
                outcome = "Player loses"
                score -= 1
                message = "New game?"
                in_play = False
        elif dealer_hand.get_value() > 21:
                outcome = "Dealer bust. Player wins"
                score += 1
                message = "New game?"
                in_play = False
        elif dealer_hand.get_value() > player_hand.get_value():
                outcome = "Player loses"
                score -= 1
                message = "New game?"
                in_play = False
        elif player_hand.get_value() > dealer_hand.get_value():
                outcome = "Player wins"
                score += 1
                message = "New game?"
                in_play = False     
     

# draw handler    
def draw(canvas):
    
    dealer_hand.draw(canvas, [-55, 240])
    player_hand.draw(canvas, [-55, 440])
    
    canvas.draw_text("Blackjack", [75, 100], 50, "White")
    canvas.draw_text("Score  " + str( score), [350, 100], 30, "White")
    canvas.draw_text("Dealer        " + str(outcome), [75, 200], 30, "White") #Player wins, Player loses, Player went bust and lost
    canvas.draw_text("Player        " + str(message), [75, 400], 30, "White") #Hit or Stand?, New game?
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [75, 289], CARD_BACK_SIZE)
        #draw back over first dealer card
      

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# and go!
deal()
frame.start()

