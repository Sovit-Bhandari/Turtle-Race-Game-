'''Name = Sovit Bhandari
U-number= U83561265
Brief discription = This is a code for race between hare and tortoise. Using the turtle function this code set the initial and 
final positon of the racer. The while loop is used to continiously assign slip or forward moving'''

import random
import turtle

# Set up the start and end lines
start = turtle.Turtle()
start.penup()
start.setpos(-100, 100)
start.pendown()
start.write("START", align="center", font=("Arial", 16, "normal"))
start.penup()
start.setpos(-100, 90)
start.pendown()
start.rt(90)
start.fd(90)
start.penup()
start.hideturtle()

end = turtle.Turtle()
end.penup()
end.setpos(100, 100)
end.pendown()
end.write("END", align="center", font=("Arial", 16, "normal"))
end.penup()
end.setpos(100, 90)
end.pendown()
end.rt(90)
end.fd(90)
end.penup()
end.hideturtle()

#Set up the command line
command = turtle.Turtle()
command.penup()
command.setpos(0,200)
command.pendown()
command.write("ON YOUR MARK.... GET SET.... GO!!!!!!!!\nAND THEY ARE OFF!",align="center", font=("Arial", 16, "normal"))
command.penup()
command.hideturtle()

# Assign initial positions for the hare and tortoise
hare_x, hare_y = -100, 50
tortoise_x, tortoise_y = -100, 0

hare = turtle.Turtle()
hare.penup()
hare.setpos(hare_x, hare_y)
hare.pendown()

tortoise = turtle.Turtle()
tortoise.shape("turtle")
tortoise.penup()
tortoise.setpos(tortoise_x, tortoise_y)
tortoise.pendown()

def turtle_position(current_position):
    num = random.randint(1, 11)
    new_position = current_position

    if 1 <= num <= 5:             #fast plod
        new_position += 3
    elif 6 <= num <= 7:           #Slip
        new_position -= 5
    else:                         #Slow plod
        new_position += 1

    #providing the boundry
    if new_position < -100:
        new_position = -100
    elif new_position > 100:
        new_position = 100

    return new_position

def hare_position(current_position):
    num = random.randint(1, 11)
    new_position = current_position

    if 1 <= num <= 2:
        new_position += 0  # Hare sleeps, no movement
    elif 3 <= num <= 4:
        new_position += 7  # Hare makes a big hop
    elif num == 5:
        new_position -= 7  # Hare makes a big slip
    elif 6 <= num <= 8:
        new_position += 1  # Hare makes a small hop
    else:
        new_position -= 1  # Hare makes a small slip

    if new_position < -100:
        new_position = -100
    elif new_position > 100:
        new_position = 100

    return new_position

time = 0
new_pos_turtle = -100
new_pos_hare = -100

while new_pos_turtle != 100 and new_pos_hare != 100:
    turtle.clear()  # Clear the previous time message
    turtle.penup()
    turtle.setpos(100, -45)
    turtle.pendown()
    turtle.write(f'Time of race: {time} seconds.', align="center", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.hideturtle()

    new_pos_turtle = turtle_position(new_pos_turtle)
    time += 1
    tortoise.setpos(new_pos_turtle, tortoise_y)
    tortoise.clear()

    new_pos_hare = hare_position(new_pos_hare)
    time += 1
    hare.setpos(new_pos_hare, hare_y)
    hare.clear()

#Determine the winner
winner = "Tortoise" if new_pos_turtle == 100 else "Hare"

# Display the winner message
turtle.penup()
turtle.setpos(160, 45)
turtle.pendown()
turtle.write(f'{winner} wins!', align="center", font=("Arial", 16, "normal"))
turtle.penup()

#Keep the window open
turtle.done()
