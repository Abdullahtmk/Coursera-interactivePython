# Echo an input field

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Handlers for input field
def get_input(txt):
    print txt
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)
frame.add_input("text",get_input,200)

# Start the frame animation
frame.start()


###################################################
# Test

###################################################
# Expected output from test

#First test input
#Second test input
#Third test input
