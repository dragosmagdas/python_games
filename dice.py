
import random
print("you found a dice use it? yes, or no")
start = input()
dice = 0
if start == "yes":
    dice = random.randint(1,6)
    print("Rolling the dice ... gave", dice)
    if dice == 1:
        print("YOU WIN")
    elif dice == 2:
        print("YOU LOSE")
    elif dice == 3:
        print("YOU WIN")
    elif dice == 4:
        print("YOU LOSE")
    elif dice == 5:
        print("YOU WIN")
    elif dice == 6:
        print("YOU LOSE")
elif start == "no":
    print("stopping game...")