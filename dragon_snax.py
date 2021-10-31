import random

cat = False
stop = False
while not stop:
    stop = True
    exitChoice = " "
    print("You are in a dark room in a mysterious castle.")
    print("In front of you are four doors you must choose one.")
    playerChoice = input("Choose 1, 2, 3, 4, 5...")
    if playerChoice == "1":
        print("you find a room full of treasure you are rich") 
        print("you win")
        print("do you dare to return to castle dragonsnax? if you do press the enter button if you don't write EXIT")
        exitChoice = input()
        if exitChoice != "EXIT":
            stop = False
    elif playerChoice == "2":    
        print("the door opens and an angry ogre hits you with his club")
        print("you lose")
        print("do you dare to return to castle dragonsnax? if you do press the enter button if you don't write EXIT")
        exitChoice = input()
        if exitChoice != "EXIT":
            stop = False
    elif playerChoice == "3":
        print("you go into the room and find a sleeping dragon")
        print("you can either:")
        print("1 try to steal some of the dragons gold")
        print("2 try to sneak around to the exit")
        dragonChoice = input("type 1, or 2,")
        if dragonChoice == "1":
            if cat == False:
                print("the dragon wakes up and eats you. you are delicious")
                print("you lose")
                print("do you dare to return to castle dragonsnax? if you do press the enter button if you don't write EXIT")
                exitChoice = input()
                if exitChoice != "EXIT":
                    stop = False
            elif cat == True:
                print("you and the cat get the dragons gold")
                print("you and the cat win!")
                print("do you dare to return to castle dragonsnax? if you do press the enter button if you don't write EXIT")
                exitChoice = input()
                if exitChoice != "EXIT":
                    stop = False
        elif dragonChoice == "2":
            print("you sneak around the dragon and escape the castle blinking in sunshine")
            print("you win")
            print("do you dare to return to castle dragonsnax? if you do press the enter button if you don't write EXIT")
            exitChoice = input()
            if exitChoice != "EXIT":
                stop = False
        else:
            print("sorry you did not enter 1, or 2,")    
    elif playerChoice == "4":
        print("you enter a room with a sphinx")
        print("it asks you to guess what number it is thinking of between 1 and 10")
        number = int(input("what number do you choose"))
        if number == random.randint(1,10):
            print("the sphinx hisses in disappointment. you guessed correctly")
            print("she must let you free")
            print("you win")
            print("do you dare to return to castle dragonsnax? if you do press the enter button if you don't write EXIT")
            exitChoice = input()
            if exitChoice != "EXIT":
                stop = False
        else:
            print("the sphinx tells you that your guess is incorrect")
            print("you are now her prisoner forever")
            print("you lose")
            print("do you dare to return to castle dragonsnax? if you do press the enter button if you don't write EXIT")
            exitChoice = input()
            if exitChoice != "EXIT":
                stop = False
    elif playerChoice == "5":
        if cat == False:
            print("you find a cat you teamup with her let's go!")
            stop = False
            cat = True
        elif cat == True:
            print("see you later")
            stop = False
            cat = False
    else:
        print("sorry you did not enter 1, 2, 3, 4, 5!")
        print("press enter to try again    write EXIT to stop the game")
        if exitChoice != "EXIT":
            stop = False           