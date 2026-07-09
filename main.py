import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
screen.title("Turtle Race Betting")
screen.bgcolor("#1b3a2b")

colors = ["red","green","yellow","black","purple","orange"]
color_list = ", ".join(color.capitalize() for color in colors)
user_bet = (screen.textinput("Make Your Bets", f"Which Turtle Wins the Race?\nChoose from: {color_list}") or "").lower()
y_positions = [-70,-40,-10,20,50,80]
all_turtle = []

track = Turtle()
track.hideturtle()
track.penup()
track.color("white")
track.pensize(3)
for line_x in (-230, 230):
    track.goto(line_x, -100)
    track.setheading(90)
    track.pendown()
    track.forward(200)
    track.penup()

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtle.append(new_turtle)

result_writer = Turtle()
result_writer.hideturtle()
result_writer.penup()
result_writer.color("white")
result_writer.goto(0, 130)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                result_writer.write(f"You WON!!! {win_color.capitalize()} turtle wins!", align="center", font=("Arial", 16, "bold"))
            else:
                result_writer.write(f"You lost! {win_color.capitalize()} turtle wins!", align="center", font=("Arial", 16, "bold"))
            break

        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)


screen.exitonclick()
