# Implementation of classic arcade game Pong
import simplegui
import random
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
paddle1_vel=[0,0]
paddle2_vel=[0,0]
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
start=0
score1=0
score2=0
# initialize ball_pos and ball_vel for new bal in middle of table

def spawn_ball(direction):
    global ball_pos, ball_vel# these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    ball_vel[1]=-random.randrange(60, 180)/60.0
    if direction == "left":
        ball_vel[0]= -random.randrange(120, 240)/60.0
    elif direction == "right":
        ball_vel[0]=random.randrange(120, 240)/60.0

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 
    score1=0
    score2=0
    paddle1_pos=[0.5*HEIGHT-HALF_PAD_HEIGHT,HALF_PAD_WIDTH,0.5*HEIGHT+HALF_PAD_HEIGHT,HALF_PAD_WIDTH]
    paddle2_pos=[0.5*HEIGHT-HALF_PAD_HEIGHT,WIDTH-HALF_PAD_WIDTH,0.5*HEIGHT+HALF_PAD_HEIGHT,WIDTH-HALF_PAD_WIDTH]
    start=random.randint(0,1)
    if start==1:
        start ="left"
    else:
        start ="right"
    spawn_ball(start)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")        
    # update ball
    if ball_pos[1] <=20 or ball_pos[1] >=380:
        ball_vel[1]=-ball_vel[1]
    elif ball_pos[0] <=28:
        if ball_pos[1]>= paddle1_pos[0] and ball_pos[1] <= paddle1_pos[2]:
            ball_vel[0]=-ball_vel[0]*1.1
            ball_vel[1]=1.1*ball_vel[1]
        else:
            score2=score2+1
            spawn_ball("right")           
    elif ball_pos[0] >= 572:
        if ball_pos[1]>= paddle2_pos[0] and ball_pos[1] <= paddle2_pos[2]:
            ball_vel[0]=-ball_vel[0]*1.1
            ball_vel[1]=ball_vel[1]*1.1
        else:
            score1=score1+1
            spawn_ball("left")      
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    # draw ball
    canvas.draw_circle([ball_pos[0],ball_pos[1]],BALL_RADIUS,2,"red","red")   
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[0]<=0 and paddle1_vel[1]<0:
        pass
    elif paddle1_pos[2]>=400 and paddle1_vel[1]>0:
        pass
    else:
        paddle1_pos[0]+=paddle1_vel[1]
        paddle1_pos[2]+=paddle1_vel[1]       
    if paddle2_pos[0]<=0 and paddle2_vel[1]<0:
        pass
    elif paddle2_pos[2]>=400 and paddle2_vel[1]>0:
        pass
    else: 
        paddle2_pos[0]+=paddle2_vel[1]
        paddle2_pos[2]+=paddle2_vel[1]        
    # draw paddles
    canvas.draw_line([paddle1_pos[1],paddle1_pos[0]],[paddle1_pos[3],paddle1_pos[2]],PAD_WIDTH,"blue")
    canvas.draw_line([paddle2_pos[1],paddle2_pos[0]],[paddle2_pos[3],paddle2_pos[2]],PAD_WIDTH,"blue")
    # draw scores
    canvas.draw_text(str(score1), (255,70 ), 30, 'grey')  
    canvas.draw_text(str(score2), (330,70 ), 30, 'grey')

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1]=-10
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel[1]=10
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel[1]=-10
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel[1]=10 

def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel[1]=0
    paddle2_vel[1]=0
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button2 = frame.add_button('Restart',new_game, 70)
# start frame
new_game()
frame.start()
