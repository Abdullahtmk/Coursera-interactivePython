# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS

     
    
# Handler for input field

def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        print("Error: Wrong input")
        
def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else:
        print("Error: Wrong input")
    

def get_guess(player_choice): 
    import random
    print("<-------------Start-------------->     ")
    print("Players Choice: %s"%(player_choice))
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print("Computer Choice: %s"%(comp_choice))
    if player_number==None:
        print("Error wrong input")
        return
    winfactor=(player_number-comp_number)%5
    if winfactor==1 or winfactor==2:
        print("Player Wins!")
    elif winfactor ==0:
        print("Tie ")
    else:
        print("Computer Wins!")

    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test



###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
