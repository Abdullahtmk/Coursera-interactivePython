# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


# helper function to start and restart the game
    
i_100=True
   
def new_game():
    # initialize global variables used in your code here
    global i_100
     
    global secret_number
    secret_number=0
    global tryy
    tryy=0
    if i_100==True:
        range100()
    else:
        range1000()
        
   


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global i_100
    i_100 = True
    print("new game Range 1-99")
    global tryy
    tryy=7
    print(str(tryy)+" total tries")
    global secret_number
    secret_number=random.randrange(0,100)
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global i_100
    i_100=False
    print("new game Range :1-999")
    global tryy
    tryy=10
    print(str(tryy)+" total tries")
    global secret_number
    secret_number=random.randrange(0,1000)
    
    
def input_guess(guess):
    # main game logic goes here
    global secret_number
    global tryy
    if tryy==0:
      print("out of trys")
      print("Number Was :"+str(secret_number))
      new_game()
    else:
      tryy-=1
        
      
      print("Guess was "+guess)
      guess=int(guess)
      if guess< secret_number:
            print("Higer")
            print(str(tryy)+" tries left")
      elif guess==secret_number:
            print("Correct")
            new_game()
      else:
            print("lower")
            print(str(tryy)+" tries left")
    if tryy==0:
        print("out of trys")
        print("Number Was :"+str(secret_number))
        new_game()
    
# create frame
frame=simplegui.create_frame("Guess the Number",200,250)
frame.add_button("range is [0-100)",range100)
frame.add_button("range is [0-1000)",range1000)
frame.add_input("Guess",input_guess,200)
# register event handlers for control elements and start frame


# call new_game 
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
