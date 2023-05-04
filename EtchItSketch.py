import turtle
#Creating a turtle and a screen
t = turtle.Turtle()
s = turtle.Screen()
#Setting the screens color, turtles color, and turtles shape
s.bgcolor("cyan")
t.color("green")
t.shape("turtle")
#Setting turles speed
speed = 5
t.speed(0)
#Defining the right function
def right():
  #Turns right 10 pixels
  t.right(10)
#Defining the left function
def left():
  #Turns left 10 pixels
  t.left(10)
#Defining the forward function
def forward():
  #Move forward 10 pixels
  t.forward(10)
#Defining the backward function
def backward():
  #Moves backward 10 pixels
  t.backward(10)
#Defining the pendown fucntion (this doesnt need to be here)
def pendown():
  t.down()
  
#Left + Right Key - Rotate
#Down + Up Key - Forward + backward
#Pendown - S (again ignore this)

#Listen indicates a readiness to accept client connection request
s.listen()
#Enables binding for key press right
s.onkey(right,'Right') 
#Enables binding for key press left
s.onkey(left,'Left')
#Enables binding for key press forward
s.onkey(forward,'Up') 
#Enables binding for key press backward
s.onkey(backward,'Down')
#Enables binding for key press down (again ignore this)
s.onkey(pendown,'S') 