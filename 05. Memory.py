# Mini-project #5 - Memory
#
# 'Introduction to Interactive Programming in Python' Course
# RICE University - coursera.org
# by Joe Warren, John Greiner, Stephen Wong, Scott Rixner
# run the code using www.codesculptor.org


# link to code http://www.codeskulptor.org/#user28_Z2UVWrGJ60_0.py




import simplegui
import random


# helper function to initialize globals
def new_game():
    global state
    global turns
    global CARDS
    global exposed
    turns = 0
    state = 0
    CARDS = range(1,9) * 2
    random.shuffle(CARDS)
    exposed = []
    for card in CARDS:
        exposed.append(False)    
     
# define event handlers
def mouseclick(pos):
  
    global state, turns, card_1, card_2, exposed, pos1, pos2
    if (state == 0) and (exposed[pos[0]//50] == False):
        turns += 1
        state = 1
        card_1 = CARDS[pos[0] // 50]
        pos1 = pos[0] // 50
        exposed[pos[0]//50] = True
   
       
    elif (state == 1) and (exposed[pos[0]//50] == False):
       state = 2
       card_2 = CARDS[pos[0] // 50]
       pos2 = pos[0] // 50
       exposed[pos[0]//50] = True 
        
    else:
        if card_1 != card_2:
            exposed[pos1] = False
            exposed[pos2] = False
       
        if exposed[pos[0]//50] == False:
            state = 1
            turns += 1
            card_1 = CARDS[pos[0] // 50]
            exposed[pos[0]//50] = True
            pos1 = pos[0] // 50
                        
# cards are 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = " + str(turns))
    p = 0
    for card in CARDS:
        canvas.draw_text(str(card), [10	+ (p * 50), 70], 50, "White")
        p += 1
    n = -1
    for card in exposed:
        n += 1
        if card == False:
            canvas.draw_polygon([[(n*50), 0], [50 + (n*50), 0], [50 + (n*50), 100], [(n*50), 100]], 5, 'Black', 'Green')
     

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# and start
new_game()
frame.start()
