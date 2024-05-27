# from turtle import Turtle, Screen
# import random
# timmy_the_turtle=Turtle()

# timmy_the_turtle.shape("turtle")


#for _ in range(4):
    #timmy_the_turtle.forward(100)
    #timmy_the_turtle.left(90)
#for _ in range(15):
  #timmy_the_turtle.forward(10)
 #timmy_the_turtle.penup()
 # timmy_the_turtle.forward(10)
  #timmy_the_turtle.pendown()

# colours=["red", "blue", "green", "pink", "orange", "yellow", "black", "brown", "maroon", "purple"]
# def draw_shape(num_sides):
#   angle=360/num_sides
#   for _ in range(num_sides):

#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(angle)

# for shape_side_n in range(3, 11):
#   timmy_the_turtle.color(random.choice(colours))
#   draw_shape(shape_side_n)

# 
# timmy_the_turtle.speed("fastest")
# timmy_the_turtle(random.choice(colours))
# timmy_the_turtle.circle(100)
# screen=Screen()
# screen.exitonclick()

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()