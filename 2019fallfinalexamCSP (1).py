
#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold
#Name
#Dieter Ruszkowski
#Date
#12/18/19

#import required libraries
import turtle as trtl

#create turtle

ike = trtl.Turtle()
#movement functions
def ike_up():
    ike.setheading(90)    #makes turtle go up
    ike.forward(10)
def ike_down():
    ike.setheading(270)      #makes turtle go down
    ike.forward(10)
def ike_right():
    ike.setheading(0)      #makes turtle go right
    ike.forward(10)
def ike_left():
    ike.setheading(180)      #makes turtle go left
    ike.forward(10)
def ike_space():           #makes turle drawing be cleared
    ike.clear()
def ike_p():
    ike.pensize(+5)      #increase drawing pen size
def ike_o():
    ike.pensize(1)       #decrease pensize
def ike_u():
    ike.penup()          #lift up the pen
def ike_q():
    ike.pendown()
    
#color/drawing functions
#i tried :(((

#bind to keypresses
wn = trtl.Screen()
wn.onkeypress(ike_up,"Up")    
wn.onkeypress(ike_down,"Down")
wn.onkeypress(ike_right,"Right")
wn.onkeypress(ike_left,"Left")
wn.onkeypress(ike_space,"space")
wn.onkeypress(ike_p,"p")
wn.onkeypress(ike_o,"o")
wn.onkeypress(ike_u,"u" )
wn.onkeypress(ike_q,"q" )

#listen
wn.listen()

#mainloop
wn.mainloop()