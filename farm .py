import time
import random

print("this is the farm, you have a pig, play in order to grow your farm")
animals = ["pig"]
money = 0
happy = 0

available_animals = {
    "pig": 10,
    "chicken": 20,
    "dog": 30,
    "cat": 40,
    "goldPig": 50,
    "goldChicken": 60,
    "goldDog": 70,
    "goldcat": 80
}

runGame = True
while runGame:
    action = input("type one of these actions (wait), (feed), (show), (buy) (exit) \n")
    if action == "show":
        print("you have money={money}$ happiness={happy} and the following animals: {animals}".format(money=money, animals=animals,  happy=happy))
    elif action == "wait":
        val = random.randint(1,11)
        time.sleep(val)
        money = money + val
        print("you received {val}$, you now have {money}$ in total".format(val=val, money=money))
    elif action == "buy":
        animal_name = input("Enter the name of the animal you want to buy: \n")
        animal_cost = available_animals.get(animal_name)
        if animal_cost == None:
            print("no animal with name: {name} found".format(name=animal_name))
            print("please choose one from the available animals: {animals}".format(animals=available_animals))
        elif animal_cost > money:
            print("not enough  money to buy {name}".format(name=animal_name))
        else:
            animals.append(animal_name)
            money = money - animal_cost
            print("you now have a {name}".format(name=animal_name))
    elif action == "feed":
        happy = happy + 10
        print("your animals happiness is now {happy}".format(happy=happy))
        if happy == 100:
            money = money + 40
            print("you now have {money}$ money".format(money=money))
        if happy == 200:
            money = money + 50
            print("you now have {money}$ money".format(money=money))
        if happy == 300:
            money = money + 60
            print("you now have {money}$ money".format(money=money)) 
    elif action == "exit":
        print("bye bye")
        runGame = False






