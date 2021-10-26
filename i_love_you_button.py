import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="press", width=40)
button.pack(padx=10, pady=10)
click = 0

def on_click(event):
    global click
    click = click + 1
    if click == 1:
        button.configure(text="i love you!")
    elif click == 2:
        button.configure(text="happy birthday!")
    elif click == 3:
        button.configure(text=":) :) :) :) :) :)")
        click = 0
button.bind("<ButtonRelease-1>", on_click)
window.mainloop()