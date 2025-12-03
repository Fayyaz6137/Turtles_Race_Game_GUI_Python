import random
from turtle import Turtle, Screen, colormode

screen = Screen()
screen.setup(width=500, height=400)

screen.title('Turtle Race')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# colors = ['red', 'blue']
turtle_list = []
user_bet = ''
race_continue = True


def set_turtles():
    global turtle_list
    turtle_list = []
    screen.clear()
    screen.bgcolor('black')
    y_axis_start = -90
    for color in colors:
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=-230, y=y_axis_start)
        y_axis_start += 40
        # new_turtle.pendown()
        new_turtle.pensize(5)
        new_turtle.speed('fastest')
        # new_turtle.shapesize(stretch_wid=2, stretch_len=2)
        turtle_list.append(new_turtle)


def set_end_line():
    end_line = Turtle()
    end_line.penup()
    end_line.goto(x=240, y=150)
    end_line.color('gray')
    end_line.pensize(10)
    end_line.pendown()
    end_line.setheading(-90)
    end_line.forward(280)
    end_line.hideturtle()


def get_continue(turtle):
    text_to_show = f'You Win! {turtle.pencolor()}\nDo you want to continue playing ? Y/N' \
        if turtle.pencolor() == user_bet \
        else f'You Lose!\nThe Winner :  {turtle.pencolor()}\nDo you want to continue playing ? Y/N'

    screen_title = 'You Win!' if turtle.pencolor() == user_bet \
        else 'You Lose!'

    choice = ''
    first_attempt = True

    while choice not in ['y', 'n']:

        choice = screen.textinput(title=screen_title, prompt=text_to_show)
        choice = choice.lower()
        if choice not in ['y', 'n'] and first_attempt:
            text_to_show = text_to_show + '\nInvalid choice.'
            first_attempt = False

        elif choice == 'y':
            return True
        elif choice == 'n':
            screen.bye()
            return False


def set_user_turtle(color):
    for turtle in turtle_list:
        if turtle.pencolor() == color:
            turtle_list[turtle_list.index(turtle)].pendown()
            # turtle_list[turtle_list.index(turtle)].shapesize(stretch_wid=2, stretch_len=2)
            break


def get_user_bet():
    prompt = 'Which bet'
    global user_bet
    user_bet = ''
    while user_bet not in colors:
        user_bet = screen.textinput(title='User Bet', prompt=prompt)
        user_bet = user_bet.lower()
        print(f'Your Bet : {user_bet}')
        if user_bet not in colors:
            prompt = 'Invalid bet. Please type a valid color'
    # set_user_turtle(user_bet)


def race_turtles():
    if user_bet:
        race_on = True
    while race_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                race_on = False
                return turtle
            else:
                turtle.forward(random.randint(1, 10))


while race_continue:
    set_turtles()
    set_end_line()
    get_user_bet()
    turtle_won = race_turtles()
    race_continue = get_continue(turtle_won)

# screen.exitonclick()

