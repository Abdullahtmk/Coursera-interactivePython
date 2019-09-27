# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def get_input(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.

# Handler for input field
def vowel(L):
    if L=="a" or L=="e" or L=="i" or L=="o" or L=="u" or L=="A" or L=="E" or L=="I" or L=="O" or L=="U":
        return True
    else:
        return False
    
    
    
def pig_latin(word):
    first_letter=word[0]
    rest_letters=word[1:]
    is_vowel=vowel(first_letter)
    if is_vowel== False:
        temp=first_letter+"ay"
        temp1=rest_letters+temp
        print temp1
    else:
        temp=word+"way"
        print temp

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Word",pig_latin,200)

# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


