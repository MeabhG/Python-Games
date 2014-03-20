# Mini-project #1 - Rock-paper-scissors-lizard-Spock
#
# 'Introduction to Interactive Programming in Python' Course
# RICE University - coursera.org
# by Joe Warren, John Greiner, Stephen Wong, Scott Rixner
# run the code using www.codesculptor.org


# link to code http://www.codeskulptor.org/#user28_nWxZg4Wc3A_0.py


import random
import math
    
#convert number to "name"
def number_to_name(number):
       if number == 0:
          return "rock"
       elif number == 1:
          return "Spock"
       elif number == 2:
          return "paper"
       elif number == 3:
          return "lizard"
       elif number == 4:
          return "scissors"
       else:
          return "Hand gesture not valid."

#convert "name" to number    
def name_to_number(name):
    if  name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Hand gesture not valid."

#create 'player' and computer hand and decide winner
def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
    num = (comp_number - player_number)%5
    print
    print "Player chooses", number_to_name(player_number)
    print "Computer chooses", number_to_name(comp_number)
    if (num == 0): 
         print "Player and computer tie!" 
    elif (num == 4) or (num == 3):     
         print "Player wins!"  
    elif (num == 2) or (num == 1):
         print "Computer wins!"
    else: 
         print "Code Fault" 
            
#test code            
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
