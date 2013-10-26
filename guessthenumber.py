# works on codeskulptor.org
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import simplegui
import random

# initialize global variables used in your code

secret_nummber = 0
num_range = 100
guesses_left = 0

# helper function to start and restart the game
def new_game():
    global secret_number, guess_allowed, guesses_left
    secret_number = random.randrange(0,num_range)
    if (num_range > 500):
        guess_allowed = 10
    else:
        guess_allowed = 7
    guesses_left = guess_allowed
    print "\nNew game... Range is from 0 to", num_range
    
    print "Number of remaining guesses is", guesses_left

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    new_game()
       
def input_guess(guess):
    # main game logic goes here	
    global my_guess,guesses_left 
    my_guess = int(guess)
    print "Your guess is ",my_guess
    if(my_guess < secret_number):
        print " Higher"
        guesses_left-=1
        print " Guess left ",guesses_left
    if(my_guess > secret_number):
        print " Lower"
        guesses_left-=1
        print " Guesses left ",guesses_left
    if(my_guess == secret_number):
        print " Correct Guess !\n" 
        new_game()
    if(guesses_left == 0):
        print " \nYou ran out of allowed guess !\n You lose !!!"
        print " Correct number was ", secret_number,"\n"
        new_game()
    
# create frame

frame = simplegui.create_frame("Guess the number",400,400)


# register event handlers for control elements
button1 = frame.add_button("Range 100",range100)
button2 = frame.add_button("range 1000",range1000)
inp = frame.add_input("Enter your guess here :",input_guess,50)


# call new_game and frame

frame.start()
new_game()
