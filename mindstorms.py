import turtle

def move_forward_and_right(move, eachs):
    for index in range(0, eachs):
        move.forward(100)
        move.right(90)

def move_forward_and_left(move, eachs):
    for index in range(0, eachs):
        move.forward(100)
        move.left(120)
    

def draw_square(square):
    square.shape("turtle")
    square.color("yellow")
    square.speed("slow")
    
    #move
    move_forward_and_right(square, 4)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    lucy = turtle.Turtle()
    lucy.shape("circle")
    lucy.color("green")
    move_forward_and_left(lucy, 2)
    lucy.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    square = turtle.Turtle()

    for i in range(1,37):
        draw_square(square)
        square.right(10)
        
    draw_circle()
    draw_triangle()

    window.exitonclick()

draw_art()
