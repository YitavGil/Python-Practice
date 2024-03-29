import colorgram
import turtle as turtle_module
import random


### get a color list
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

turtle_module.colormode(255)
michelangelo = turtle_module.Turtle()
michelangelo.speed("fastest")
michelangelo.penup()
michelangelo.hideturtle()
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

michelangelo.setheading(225)
michelangelo.forward(300)
michelangelo.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    michelangelo.dot(20, random.choice(color_list))
    michelangelo.forward(50)

    if dot_count % 10 == 0:
        michelangelo.setheading(90)
        michelangelo.forward(50)
        michelangelo.setheading(180)
        michelangelo.forward(500)
        michelangelo.setheading(0)








screen = turtle_module.Screen()
screen.exitonclick()