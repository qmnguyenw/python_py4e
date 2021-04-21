Create pong game using Python – Turtle



Pong is one of the most famous arcade games, simulating table tennis. Each
player controls a paddle in the game by dragging it vertically across the
screen’s left or right side. Players use their paddles to strike back and
forth on the ball.

Turtle is an inbuilt graphic module in Python. It uses a panel and pen to
depict illustrations.

**Below are the steps used:**

  *  **Step 1)** Create two paddles A and B on the left and right side of the screen.
  *  **Step 2)** Create a ball.
  *  **Step 3)** Create an event to move the paddle vertically on pressing a certain key.
  *  **Step 4)** Create the function to update the score after each player misses a collision.

 **Below is the program to create Paddle and Ball:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Import required library

import turtle

 

# Create screen

sc = turtle.Screen()

sc.title("Pong game")

sc.bgcolor("white")

sc.setup(width=1000, height=600)

 

 

# Left paddle

left_pad = turtle.Turtle()

left_pad.speed(0)

left_pad.shape("square")

left_pad.color("black")

left_pad.shapesize(stretch_wid=6, stretch_len=2)

left_pad.penup()

left_pad.goto(-400, 0)

 

 

# Right paddle

right_pad = turtle.Turtle()

right_pad.speed(0)

right_pad.shape("square")

right_pad.color("black")

right_pad.shapesize(stretch_wid=6, stretch_len=2)

right_pad.penup()

right_pad.goto(400, 0)

 

 

# Ball of circle shape

hit_ball = turtle.Turtle()

hit_ball.speed(40)

hit_ball.shape("circle")

hit_ball.color("blue")

hit_ball.penup()

hit_ball.goto(0, 0)

hit_ball.dx = 5

hit_ball.dy = -5  
  
---  
  
 __

 __

