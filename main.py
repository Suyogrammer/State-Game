import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Guess Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.tolist()
print(state_list)

input_state = screen.textinput(title="Guess the state", prompt="Enter a state name")
print(input_state.title())

if input_state in state_list:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == input_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(input_state.title())

screen.exitonclick()