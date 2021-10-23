runGame = True
while runGame == True:
    none = input()
    for x in range(0,9):
        print("welcome home!")
    none = input()
    for x in range(0,9):
        print("i love you")
    none = input()
    for x in range(0,9):
        print("you are the best dad!")
    
    none = input()
    for x in range(0,9):
        print(":)")
    print("play again? yes or no")
    runningGame = input()
    if runningGame == "yes":
        runGame = True
    elif runningGame == "no":
        print("ok stopping game.....")
        runGame = False
