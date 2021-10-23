print("you are the commander of the lion troop")
print("choose a command farm, castle, or mars")
choice = input()
if choice == "farm":
    print("you can choose an action fight or steal:")
    action1 = input()
    if action1 == "fight":
        print("the farmers had no chance")
        print("YOU WIN")
    elif action1 == "steal":
        print("a farmer catches you")
        print("YOU LOSE")
    else:
        print("sorry you did not enter fight, or steal")

elif choice == "castle":
    print("a guard finds you")
    print("YOU LOSE")
elif choice == "mars":
    print("you can choose an action fight, or power up")
    action2 = input()
    if action2 == "fight":
        print("you had no chance")
        print("YOU LOSE")
    elif action2 == "power up":
        print("you are powered up")
        print("fight the castle? Y,N")
        action3 = input()
    if action3 == "Y":
        print("YOU WIN")
    elif action3 == "N":
            print("YOU LOSE")
    else:
        print("sorry you did not enter fight, or power up")

else:
    print("sorry you did not enter farm, castle, or mars")
    