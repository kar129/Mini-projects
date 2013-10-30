## This is an Interactive Calculator program which performs basic arithmatic operatoins.
## Code works on Codeskulptor and can be found on below link.
## http://www.codeskulptor.org/#user21_CtQkyes5HCAt1A4.py


#making a interactive calculator

import simplegui

store = 0
operand = 0
remainder = 0

# Every function is an event handler here and handles a particular event as assgined to them.

# This function acts as an output handler button which prints the value stored at store variable and current
#    value of operand.
def output():
    print "store = ", store
    print "operand = ", operand
    print""
    
# This function represents a Swap button on canvas and written to swap the values of operand and store.
def swap():
    global operand,store
    operand,store = store,operand
    output()

# Add button on the canvas lead to execute this code.    
def add():
    global operand,store
    store = store + operand
    output()

# Subtract button on the canvas lead to execute this code.       
def sub():
    global operand,store
    store = store - operand
    output()
# Multiply button on the canvas lead to execute this code.   
def mul():
    global store,operand
    store = store * operand
    output()
    
# Division button on the canvas lead to execute this code.   
def division():
    global operand, store
    store =store/operand
    output()
    
# Modulus button on the canvas lead to execute this code.   
def modulus():
    global operand, store, remainder
    remainder = store % operand
    print "Remainder",remainder
    
# Imput event handler for input field on the canvas.
def enter(input):
    '''(str) -> 
    
    This input handler take a input as a string input and store it into operand.
    '''
    global operand
    operand = float(input)
    output()

#Just to draw on Canvas.    
def draw(canvas):
    canvas.draw_text("Calculator",(10,50),50,'Blue')
    canvas.draw_text("-github @mk1727",(10,100),50,'Blue')
f = simplegui.create_frame("Calculator",500,500)
f.add_button("Print",output,70)
f.add_button("Swap",swap,70)
f.add_button("Add",add,70)
f.add_button("Multiply",mul,70)
f.add_button("Subtract",sub,70)
f.add_button("Divide",division,70)
f.add_button("Remainder",modulus,70)
f.add_input("Input",enter,70)
f.set_draw_handler(draw)

f.start()
