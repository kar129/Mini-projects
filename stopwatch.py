# "Stopwatch: The Game"
# Live Program can be found @ http://www.codeskulptor.org/#user22_EVrQ76mUQJywdkP.py

import simplegui

# define global variables

tenths = 0
successful_clicks = 0
total_clicks = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    t = t//10
    seconds = t % 100
    t = t//100
    minutes = t
    
    if seconds >= 60:
        seconds %= 60
        minutes+=1
    
    if minutes >= 60:
        minutes %= 60
    
    
    if minutes < 10:
        mins = "0"+str(minutes)
    else:
        mins = str(minutes)
    
    
    if seconds < 10:
        secs = "0"+str(seconds)
    else:
        secs = str(seconds)
        
    return mins+":"+secs+"."+str(tenths)
                   
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    
def stop():
    global total_clicks, successful_clicks
    if timer.is_running():
        total_clicks += 1
        if tenths % 10 == 0:
            successful_clicks += 1

        timer.stop()
    
def reset():
    global tenths, successful_clicks, total_clicks
    tenths = 0
    successful_clicks = 0
    total_clicks = 0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval

def ticker():
    global tenths
    tenths+=1
    
    
# define draw handler

def draw(canvas):
    global string
    canvas.draw_text(str(successful_clicks)+"/"+str(total_clicks),(255,30),30, 'Green')
    canvas.draw_text(format(tenths),(90,125),50,'White')
    
# create frame

frame = simplegui.create_frame("Stop Watch",300,220)
timer = simplegui.create_timer(100,ticker)


# register event handlers

frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.set_draw_handler(draw)


# start frame

frame.start()

# Please remember to review the grading rubric
