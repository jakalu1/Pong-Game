"""
Pong
* this is the pong game that I created. This file houses the frontend and backend to the game. 
"""

import turtle
import pygame

#initializing/preparing the pygame module so that we can work with it
pygame.init()
bounce_sound = pygame.mixer.Sound('bounce1.mp3') #creating an object of the pygame Sound class and passing our sound file name as a parameter to this


win = turtle.Screen() #create an object of the turtle module while also creating a window!
win.title('Pong by Jeremiah via Python') #naming the window
win.bgcolor('dark blue') #background color of the window
win.setup(width=800, height=600) #in pixels
win.tracer(0) #stops the window from auto updating at the default rate. this allows us to manually update it and speed up the rate in which we refresh the screen



#Score Tracker
p1_score = 0
p2_score = 0
    

#paddle A code. syntax = module.ClassName()
paddle_a = turtle.Turtle() #making paddle A a turtle object
paddle_a.speed(0) #the speed of animation. 0 is the max possible speed! (required for turtle graphics)
paddle_a.color('white')
paddle_a.shape('square') #by default, a 'square's dimension is 20 by 10
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5) #dimension is now 100 by 10 pixels
paddle_a.penup() #turtle module objects naturally draw lines as they are moving, but when we do pen up, we disable that feature
paddle_a.goto(-350, 0) #(x, y) coordinates on the screen. if x was 0 and y was 0, it would be in the middle of the screen. 


#paddle B code
paddle_b = turtle.Turtle() 
paddle_b.speed(0) 
paddle_b.color('white')
paddle_b.shape('square') 
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5) 
paddle_b.penup() 
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle() 
ball.speed(0) 
ball.color('white')
ball.shape('circle') 
ball.penup() 
ball.goto(0, 0)
#moving the ball. we need it to move initially, bounce off the top and bottom, and the paddles
ball.dx = 0.15 #means everytime the ball moves, it moves by 0.9 pixels. x and y are positive here so it is initially going to move up and to the right
ball.dy = -0.15

def go():
    ball.dx = 0.15
    ball.dy = -0.15

def ag_reset():
    ball.goto(0,0)
    ball.dx = 0
    ball.dy = 0


#Pen
pen = turtle.Turtle()
pen.speed(0) #animation speed
pen.color('white')
pen.penup() #we don't want it to show a line while its moving
pen.hideturtle() #we don't want to see the pen, we just want to see the text that its going to write
pen.goto(0, 260)
pen.write('Player 1: 0 Player 2: 0', align='center', font=('Courier', 20,'normal'))

#for the instructions on the top right of the screen
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color('white')
pen2.penup()
pen2.hideturtle()
pen2.goto(-320, 260)
pen2.write('''r: reset ball\ng: resume ball''', align='center', font=('Courier', 12, 'normal'))


#functions to move the paddles using the keyboard
def paddle_a_up(): #we r lucky because in this game we don't move on the x axis
    y = paddle_a.ycor() #method that returns the y coordinate of the object u specify. we are assigning that to y variable
    y += 25 #going up makes the ycor increase and going down makes in decrease. so we add 20 pixels to the y coordinate
    paddle_a.sety(y) #now we set paddle_a's ycor to the updated y coordinate

def paddle_a_down():
    y = paddle_a.ycor() #method that returns the y coordinate of the object u specify. we are assigning that to y variable
    y -= 25 #going up makes the ycor increase and going down makes in decrease. so we add 20 pixels to the y coordinate
    paddle_a.sety(y) #now we set paddle_a's ycor to the updated y coordinate

def paddle_b_up(): 
    y = paddle_b.ycor() 
    y += 25 
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 25
    paddle_b.sety(y)

#keyboard binding
win.listen() #this tells the program to listen for keyboard input (remember win is our object we use to access turtle classes)
win.onkeypress(paddle_a_up, 'w') #this binds the function of paddle a moving up 20 pixels, to the 'w' key. Basically, when the user presses 'w', call the fuction paddle_a_up
win.onkeypress(paddle_a_down, 's') #likewise it does this for the paddle_a_down function. IT HAS TO BE LOWERCASE. it doesn't listen to capslock if it is 'w' or 's'
win.onkeypress(paddle_b_up, 'Up') #Up is the up arrow and Down is the down arrow
win.onkeypress(paddle_b_down, 'Down')
win.onkeypress(ag_reset, 'r')
win.onkeypress(go, 'g')


#every game needs something called main game loop (meat and potatoes)
while True:
    win.update() #every time the loop runs, it updates the screen (keeps the screen on basically)


    #as long as the game is running, move the ball. 
    ball.setx(ball.xcor() + ball.dx)#now tell the balls y and x coordinates to update and move 0.15 pixels (from the ball.dx and dy functions above)
    ball.sety(ball.ycor() + ball.dy)

#border checking. (make it bounce once we get to a certain point)
    if ball.ycor() > 281: #allowing for it to pass the border by 1 pixel so that when it does, it executes the code below!
        ball.sety(280) #the second the ball's ycor exceeds the limit, it resets it to this coordinate and the line of code below tells it what to do next
        ball.dy *= -1 #dy means delta y or change in y. negative means it goes downwards. so it now sets the change in why in the downwards/opposite direction when hitting the top border
        bounce_sound.play() #plays that bounce sound that we initialized with the pygame module up at the beginning of the program

    if ball.ycor() <- 281:
        ball.sety(-280)
        ball.dy *= -1
        bounce_sound.play()

    if ball.xcor() > 400: #everytime the ball fully passes the right border:
        ball.goto(0, 0) #reset the ball to go to 0 
        ball.dx *= -1 #and make it so that it now moves in the opposite way by reversing its dx!
        p1_score += 1
        pen.clear() #clear the score that is already on the screen then print the new score
        pen.write(f'Player 1:{p1_score} Player 2: {p2_score}', align='center', font=('Courier', 20,'normal'))

    if ball.xcor() < -400: #everytime the ball fully passes the left border:
        ball.goto(0, 0) #reset the ball to go to 0
        ball.dx *= -1 #and make it so that it now moves in the opposite way by reversing its dx!
        p2_score += 1
        pen.clear()
        pen.write(f'Player 1:{p1_score} Player 2: {p2_score}', align='center', font=('Courier', 20,'normal'))

#Making both paddles not move off the screen!
    if paddle_a.ycor() < -240: 
        paddle_a.sety(-240)
    if paddle_a.ycor() > 248:
        paddle_a.sety(248)

    if paddle_b.ycor() < -240: 
        paddle_b.sety(-240)
    if paddle_b.ycor() > 248:
        paddle_b.sety(248)


#colliding with paddles: (compare the x and y of the ball and paddles to see if they are touching)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx*= -1
        bounce_sound.play()
    if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx*= -1
        bounce_sound.play()
