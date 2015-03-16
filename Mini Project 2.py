import simplegui
import random
messege = "Guess a number from 1 to 100 "
# helper function to start and restart the game
def new_game():
    print 'New Game!'
    range100()


# define event handlers for control panel
def range100():
    global secret_number,count,messege 
    count = 7
    secret_number = random.randint(0,100)
    print "Game starts "
    messege = "Guess a number from 1 to 100 "
    print messege,'\n',"Number of remaining guess:",count,'\n'

def range1000():
    global secret_number,count,messege 
    count = 10
    secret_number = random.randint(0,1000)
    print "Game starts "
    messege = "Guess a number from 1 to 1000 "
    print messege,"\n","Number of remaining guess:",count,'\n'
    
def input_guess(guess):
    compare = int(float(guess))
    global count,messege
    if count >0: 
        print "Guess was",compare
        if compare > secret_number:
            print "Lower!"
            print "Number of remaining guesses is",count-1,"\n"
            count=count-1
        elif compare < secret_number:
            print "Higher!"
            print "Number of remaining guesses is",count-1,"\n"
            count=count-1
        elif compare == secret_number:
            print  "Corret! Congrats!\nGame Restarts\n.\n.\n."
            if messege =="Guess a number from 1 to 1000 ":
                range1000()
            else:
                range100()
    if count==0:
        print "You have run out of chances!\nThe number is",secret_number,'\n'
        print "Game Restarts\n.\n.\n."
        if messege =="Guess a number from 1 to 1000 ":
            range1000()
        else:
            range100()
    
def draw_handler(canvas):
    canvas.draw_text(messege, (0, 100), 20, 'Red')   

    
# create frame
frame = simplegui.create_frame("Guess The Number", 300, 200)
button1 = frame.add_button('Restart Game', new_game)
button2 = frame.add_button('Set Range 0 to 100', range100)
button3 = frame.add_button('Set Range 0 to 1000', range1000)
inp = frame.add_input('What is your GUESS', input_guess,100)
frame.set_draw_handler(draw_handler)

new_game()
frame.start()
