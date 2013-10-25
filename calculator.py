## This is an Interactive Calculator program which performs basic arithmatic operatoins.
## Code works on Codeskulptor and can be found on below link.
## http://www.codeskulptor.org/#user21_CtQkyes5HCAt1A4.py


#making a interactive calculator

import simplegui

store = 0
operand = 0
remainder = 0

def output():
    print "store = ", store
    print "operand = ", operand
    print""
    
def swap():
    global operand,store
    operand,store = store,operand
    output()
    
def add():
    global operand,store
    store = store + operand
    output()
    
def sub():
    global operand,store
    store = store - operand
    output()

def mul():
    global store,operand
    store = store * operand
    output()
    
def division():
    global operand, store
    store =store/operand
    output()
    
def modulus():
    global operand, store, remainder
    remainder = store % operand
    print "Remainder",remainder
    
def enter(input):
    global operand
    operand = float(input)
    output()
    
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
