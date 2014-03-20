# Mini-project #4 - Pong
#
# 'Introduction to Interactive Programming in Python' Course
# RICE University - coursera.org
# by Joe Warren, John Greiner, Stephen Wong, Scott Rixner
# run the code using www.codesculptor.org


# link to code http://www.codeskulptor.org/#user28_AhBx1lwbdA_5.py


import simplegui
import random

# initialize globals 
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [2.0,-2.0]
paddle1_pos = [160, 240]
paddle2_pos = [160, 240]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
score1 = 0 
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
def spawn_ball(direction):
    global ball_pos, ball_vel 
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel[0] = float(random.randrange(120, 240))/100
    ball_vel[1] = float(random.randrange(60, 180))/100
    if direction:
       ball_vel[1] = -ball_vel[1]
    else:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel  # these are numbers
    global score1, score2  # these are ints
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [2.0,-2.0]
    paddle1_pos = [160, 240]
    paddle2_pos = [160, 240]
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    score1 = 0 
    score2 = 0
    
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_text(str(score1), [150, 75], 50, "White")
    c.draw_text(str(score2), [450, 75], 50, "White")
    
   
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
       ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= (HEIGHT -1)-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
   
    # code about bat behind edge
    elif (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and (ball_pos[1] >= paddle1_pos[0]) and (ball_pos[1] <= paddle1_pos[1]):
        ball_vel[0] = - ball_vel[0]
        ball_vel[0] = ball_vel[0] * 1.1
        ball_vel[1] = ball_vel[1] * 1.1
    elif (ball_pos[0] >= (WIDTH -1)-BALL_RADIUS - PAD_WIDTH) and (ball_pos[1] >= paddle2_pos[0]) and (ball_pos[1] <= paddle2_pos[1]):
        ball_vel[0] = - ball_vel[0]
        ball_vel[0] = ball_vel[0] * 1.1
        ball_vel[1] = ball_vel[1] * 1.1
        
        
    # ball goes over the edge
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        score2 += 1
        spawn_ball(RIGHT)
    elif ball_pos[0] >= (WIDTH -1)-BALL_RADIUS - PAD_WIDTH:
        score1 += 1
        spawn_ball(LEFT)
        
    
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    
    # update paddle's vertical position, keep paddle on the screen    
    if ((paddle1_pos[0] + paddle1_vel[0]) >= 0) and ((paddle1_pos[0] + paddle1_vel[0]) <= HEIGHT -81): 
        paddle1_pos[0] += paddle1_vel[0]
        paddle1_pos[1] += paddle1_vel[1]
         
    if ((paddle2_pos[0] + paddle2_vel[0]) >= 0) and ((paddle2_pos[0] + paddle2_vel[0]) <= HEIGHT -81): 
        paddle2_pos[0] += paddle2_vel[0]
        paddle2_pos[1] += paddle2_vel[1]
  
        
    # draw paddles
    paddle1= c.draw_line([PAD_WIDTH/2, paddle1_pos[0]],[PAD_WIDTH/2, paddle1_pos[1]], PAD_WIDTH, "White")
    paddle2= c.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos[0]],[WIDTH - PAD_WIDTH/2, paddle2_pos[1]], PAD_WIDTH, "White")
    
 
def keydown(key):
    global paddle1_vel, paddle2_vel
   
    acc = 3
    if  key == (simplegui.KEY_MAP["w"]):
        paddle1_vel[0] -= acc
        paddle1_vel[1] -= acc 
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[0] += acc 
        paddle1_vel[1] += acc 
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[0] += acc
        paddle2_vel[1] += acc 
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= acc 
        paddle2_vel[1] -= acc 
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if  key == (simplegui.KEY_MAP["w"]):
        paddle1_vel = [0,0]
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = [0,0]
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = [0,0]
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = [0,0]


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 100)

# start frame
new_game()
frame.start()
