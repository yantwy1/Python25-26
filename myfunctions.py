import turtle
bob = turtle.Turtle()

#snowflake
def snowflake(dist,angle, num):
  for times in range(num):
    bob.color("white")
    bob.forward(dist)
    bob.left(angle)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()
    
def crater(dist,angle,num):
  for times in range(num):
    bob.color("grey")
    bob.forward(dist)
    bob.left(angle)
  
