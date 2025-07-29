import turtle
import pandas

panda = pandas.read_csv("50_states.csv")
states = panda.state.to_list()
score = 0

toby = turtle.Turtle()
toby.penup()
toby.hideturtle()

screen = turtle.Screen()
screen.title("Name the States")
screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

answered = []
while True:
    guess = screen.textinput(f"{score}/50 States Correct", "Enter a State Name?").title()
    if guess in states:
        if guess not in answered:
            answered.append(guess)
            score += 1
            state = panda[panda.state == guess]
            toby.goto(int(state.x.iloc[0]), int(state.y.iloc[0]))
            toby.write(guess, font=("Arial", 5, "bold"))
    elif guess == "Exit":
        '''Code with List Comprehension'''
        not_answered = [state for state in panda["state"] if state not in answered]

        data = pandas.DataFrame(not_answered)
        data.to_csv("Missing States.csv")
        break

    if score == 50:
        toby.goto(0, 0)
        toby.color("yellow")
        toby.pensize(5)
        toby.write("You Win!", False, "center", ("Arial", 50, "bold"))
        screen.exitonclick()