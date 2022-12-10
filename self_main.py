from turtle import Turtle,Screen
import random
import time

screen = Screen()
screen.setup(600, 600)
number_of_turtle = screen.textinput(title = 'how many turtle race you want', prompt = 'you can not enter number greater then six')
number_of_turtle = int(number_of_turtle)
if number_of_turtle == 0 or number_of_turtle == 1:
    print('race is not possible')
    exit()

colors = ['red','blue','orange','green','pink','yellow']
user_bet = screen.textinput(title = 'enter your bet', prompt = f'enter the color on which you want to bet.\n available colors are:{", ".join(colors[0:number_of_turtle])}')
y_location = [-70, -50, -30, -10, 10, 30]
all_turtle = []

for i in range(0, number_of_turtle):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,y_location[i])
    time.sleep(1)
    all_turtle.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230 :
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print('you won the bet')
            else:
                print(f'you lost the bet winnig colors is {winning_color}')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)






