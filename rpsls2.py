# Rock-paper-scissors-lizard-Spock template
import random
import simplegui
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# helper functions

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
        print " You entered an invalid number."
        
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    if name == "rock":
        return 0
    elif name == "Spock" or name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print " You entered an invalid name."
    
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below
    print "Player chooses "+name
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    print "Computer chooses "+number_to_name(comp_number)
    # compute difference of player_number and comp_number modulo five
    diff = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if diff > 2:
        winner = "Computer"
    elif diff == 0:
        winner = "No one"
    else:
        winner = "Player"
    # convert comp_number to name using number_to_name
    name = number_to_name(comp_number)
    # print results
    if diff == 0:
        print "Player and Computer tie! \n\n"
    else:
        print winner + " wins! \n\n"
    

# frame settings 
frame = simplegui.create_frame("RPSLS",100,100)
frame.add_input("What you choose, enter here :",rpsls,100)

frame.start()
# always remember to check your completed program against the grading rubric


