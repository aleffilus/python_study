import turtle

def move_forward_and_right(move, eachs):
    for index in range(0, eachs):
        move.forward(100)
        move.right(90)

def move_forward_and_left(move, eachs):
    for index in range(0, eachs):
        move.forward(100)
        move.left(120)
    
def draw_o():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_a(draw):
    draw.down()
    draw.left(90)
    draw.forward(100)
    draw.right(90)
    draw.forward(50)
    draw.right(90)
    draw.forward(50)
    draw.right(90)
    draw.forward(50)
    draw.back(50)
    draw.left(90)
    draw.forward(50)
    draw.left(90)
    draw.up()
    draw.forward(30)

def drawL(draw):
    draw.down()
    draw.left(90)
    draw.forward(100)
    draw.back(100)
    draw.right(90)
    draw.forward(50)
    draw.up()
    draw.forward(30)

def draw_art():
    draw = turtle.Turtle()
    draw.speed(1)
    draw_a(draw)
    drawL(draw)

draw_art()
