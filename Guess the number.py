# Mini-project #2 - Guess the number
#
# 'Introduction to Interactive Programming in Python' Course
# RICE University - coursera.org
# by Joe Warren, John Greiner, Stephen Wong, Scott Rixner
# run the code using www.codesculptor.org


# link to code http://www.codeskulptor.org/#user28_5wDR9vkBbB_0.py


# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math


# initialize global variables 
num_range = 100
secret_num = 0
remaining = 0

# helper function to start and restart the game
def new_game():
    if num_range == 100:
        range100()
    elif num_range == 1000:
        range1000()
    else:
        print "Num_range fault!"


# button that changes range to range [0,100) and restarts
def range100():
    global secret_num
    secret_num = random.randrange(1, 101)
    global remaining
    remaining = 7
    global num_range
    num_range =100
    
    print
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is 7"

# button that changes range to range [0,1000) and restarts
def range1000():
    global secret_num
    secret_num = random.randrange(1, 1001)
    global remaining
    remaining = 10
    global num_range
    num_range =1000

    print
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is 10"
    
#input player guess check to see if right update guesses remaining    
def get_input(guess):
    
     player_num = int(guess)
    
     global remaining
     if remaining >= 1:
        remaining = remaining -1
     else:
          print "Remaining Error"      
     
     print
     print "Guess was", player_num
     print "Number of remaining guesses is", remaining
    
     if secret_num == player_num:
        print "Correct!"
        new_game() 
     elif (secret_num > player_num) and (remaining == 0):
        print "Higher!"
        new_game()
     elif (secret_num < player_num)  and (remaining == 0):
        print "Lower!"
        new_game()
     elif secret_num > player_num :
        print "Higher!"
     elif secret_num < player_num:
        print "Lower!"   
     else:
        print "Error!"
     
    
# create frame
f=simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements
f.add_button("Range is (0, 100)", range100, 200)
f.add_button("Range is (0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# call new_game and start frame
f.start()
new_game()

