import tkinter
import random
from typing import Sequence
gameOver = False
score = 0
squaresToClear = 0

bombfield = []


def play_dodge_the_bombs():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()


def create_bombfield(bombfield):
    global squaresToClear
    for row in range(0, 10):
        rowList = []
        for column in range(0, 10):
            if random.randint(1, 100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear = squaresToClear + 1
        bombfield.append(rowList)
    printfield(bombfield)


def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)


def layout_window(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1, 100) < 25:
                square = tkinter.Label(window, text="    ", bg="darkgreen")
            elif random.randint(1, 100) > 75:
                square = tkinter.Label(window, text="    ", bg="seagreen")
            else:
                square = tkinter.Label(window, text="    ", bg="green")
            square.grid(row=rowNumber, column=columnNumber)


play_dodge_the_bombs()
