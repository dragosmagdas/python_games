import tkinter

print("to draw hold down the left mouse button and move your mouse around")
print("to change your brush color click on one of the colours")
none = input()
window = tkinter.Tk()

canvas = tkinter.Canvas(window, width=750, height=500, bg="white")
canvas.pack()

lastX, lastY = 0,0
colour = "black"

button = tkinter.Button(window, text="press for mouse coordinates", width=40)
button.pack(padx=10, pady=10)

label = tkinter.Label(window, text="Coordinates!")
label.pack(padx=10, pady=10)

printEvents = False

def on_btn_click(event):
    global printEvents
    printEvents = not printEvents

button.bind("<ButtonRelease-1>", on_btn_click)

def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y
    if printEvents:
        label["text"] = str.format("X: {x}, Y: {y}", x = lastX, y=lastY)
        #print(event)

def on_click(event):
    store_position(event)


def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill = colour, width = 3)
    store_position(event)

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id = canvas.create_rectangle(10, 60, 30, 80, fill="black")
white_id = canvas.create_rectangle(10, 85, 30, 105, fill="white")
green_id = canvas.create_rectangle(10, 110, 30, 130, fill="green")
yellow_id = canvas.create_rectangle(10, 135, 30, 155, fill="yellow")
pink_id = canvas.create_rectangle(10, 160, 30, 180, fill="pink")
orange_id = canvas.create_rectangle(10, 185, 30, 205, fill="orange")
cyan_id = canvas.create_rectangle(10, 210, 30, 230, fill="cyan")

def set_colour_red(event):
    global colour
    colour="red"

def set_colour_blue(event):
    global colour
    colour="blue"

def set_colour_black(event):
    global colour
    colour="black"

def set_colour_white(event):
    global colour
    colour="white"

def set_colour_green(event):
    global colour
    colour="green"

def set_colour_yellow(event):
    global colour
    colour="yellow"

def set_colour_pink(event):
    global colour
    colour="pink"

def set_colour_orange(event):
    global colour
    colour="orange"

def set_colour_cyan(event):
    global colour
    colour="cyan"

canvas.tag_bind(red_id, "<Button-1>", set_colour_red)
canvas.tag_bind(blue_id, "<Button-1>", set_colour_blue)
canvas.tag_bind(green_id, "<Button-1>", set_colour_green)
canvas.tag_bind(yellow_id, "<Button-1>", set_colour_yellow)
canvas.tag_bind(pink_id, "<Button-1>", set_colour_pink)
canvas.tag_bind(orange_id, "<Button-1>", set_colour_orange)
canvas.tag_bind(cyan_id, "<Button-1>", set_colour_cyan)
canvas.tag_bind(black_id, "<Button-1>", set_colour_black)
canvas.tag_bind(white_id, "<Button-1>", set_colour_white)  

window.mainloop()