import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.setup(800, 600)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = Turtle()

data_states = pd.read_csv("50_states.csv")
answer = screen.textinput("Guess the State", "What's the name of another state?")
answer = answer.title()
states = data_states.state.to_list()
guessed_states = []
score = 0

while score < 50:

    if answer == "Exit":

        states_learn = [guess for guess in states if guess not in guessed_states]

        new_dict = {"States": states_learn}
        df = pd.DataFrame(states_learn)

        df.to_csv("states_to_learn.csv")

        break

    if answer in states and answer not in guessed_states :
        score += 1
        guessed_states.append(answer)
        row = data_states[data_states["state"] == answer]

        x_cor = row["x"].iloc[0]
        y_cor = row["y"].iloc[0]

        pen.hideturtle()
        pen.penup()
        pen.goto(x_cor, y_cor)
        pen.write(answer)

    answer = screen.textinput(f"{score}/50 States correct", "What's the name of another state?")
    answer = answer.title()


turtle.mainloop()
