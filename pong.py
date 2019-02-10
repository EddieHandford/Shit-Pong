# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:00:59 2019

@author: Eddie
"""
import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Eddie")
wn.bgcolor("blue")
wn.setup(width=800 , height=600)
wn.tracer(0)



#while True:
#    wn.update()
#    
    
    
    
#creating a paddle
    
#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0) # max speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0) # max speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#ball
ball = turtle.Turtle()
ball.speed(0) # max speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)


# Score
score_a = 0
score_b = 0


ball.dx = (score_a+score_b) + 0.03
ball.dy = (score_a+score_b) + 0.03 # max move is by 2 pixels



#pen
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PlayerA: 0  PlayerB: 0" , align="center" , font=("Courier" , 24 , "normal"))






#function for moving objects

def paddle_a_up():
    y = paddle_a.ycor() #assidle paddle y coor to a "y"
    y += 20 # goes up by 20 pixels when you press up
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor() #assidle paddle y coor to a "y"
    y -= 20 # goes up by 20 pixels when you press up
    paddle_a.sety(y)
    
    
def paddle_b_up():
    y = paddle_b.ycor() #assidle paddle y coor to a "y"
    y += 20 # goes up by 20 pixels when you press up
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor() #assidle paddle y coor to a "y"
    y -= 20 # goes up by 20 pixels when you press up
    paddle_b.sety(y)
    
    
wn.listen()

wn.onkeypress(paddle_a_up, "w")

wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "i")

wn.onkeypress(paddle_b_down, "k")




while True:
    wn.update()
    
    
    
#    ball.dx = (score_a+score_b)*0.01 + 0.03
#    ball.dy = (score_a+score_b)*0.01 + 0.03 # max move is by 2 pixels
    
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    #border of game check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
        
        
        
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
        
        
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx += 0.01
        ball.dy += 0.01
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a , score_b) , align="center" , font=("Courier" , 24 , "normal"))
        winsound.PlaySound("reload.wav" , winsound.SND_ASYNC)
         
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dx += 0.01
        ball.dy += 0.01
        
        score_b += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a , score_b) , align="center" , font=("Courier" , 24 , "normal"))
        winsound.PlaySound("reload.wav" , winsound.SND_ASYNC)
        
#paddle hitting the ball
        
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
        
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav" , winsound.SND_ASYNC)
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    