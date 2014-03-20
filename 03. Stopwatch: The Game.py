# Mini-project #3 - Stopwatch: The Game
#
# 'Introduction to Interactive Programming in Python' Course
# RICE University - coursera.org
# by Joe Warren, John Greiner, Stephen Wong, Scott Rixner
# run the code using www.codesculptor.org


# link to code http://www.codeskulptor.org/#user28_d7J36lUjTE_0.py


import simplegui

#global variables
go = 0
time = 0
sec_10 = "0"
clock = "0:00.0"
attempt = 0
success = 0

#formats time correctly
def format():
    global time
    global clock
    global sec_10
    min = str(time//600)
    sec =str((time%600)/10)
    if int(sec) <= 9:
       sec = "0"+ sec
    sec_10 = str((time % 600) -(int(sec)*10))
    clock = min + ":" + sec + "." + sec_10
    

def start():
    global go
    go = 1
    

def stop():
    global go
    global attempt
    global success
    global sec_10
    go = 0
    attempt += 1
    if sec_10 == "0":
        success += 1
    else:
        success = success
  

def reset():
    global go
    global time
    global attempt
    global success
    time = 0
    go = 1
    attempt = 0
    success = 0
   
#called by the timer. Updates the time if start True.
def tick():
    global go
    global time
    if go == 1:
        time += 1
        format()
    else:
        time = time


def draw_handler(canvas):
    canvas.draw_text(clock, [70, 110], 25, "White")
    canvas.draw_text(str(attempt) +"/" +str(success), [165, 25], 20, "White")

# create frame    
frame = simplegui.create_frame("Timer", 200, 200)

# register event handlers for control elements
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw_handler)

# call new_game and start frame
frame.start()
timer.start()

