aliens = 2
print("quickly! aliens are invading the planet.")
print("hope you know the password for earths sake")
print()
print("____________________________________________")  
print("      WELCOME TO GLOBAL DEFENSE NETWORK     ")
print("____________________________________________")
print()
guess = int(input("please enter the password:  "))
while guess != aliens:
    print()
    print("INCORECT PASSWORD.")
    print()
    aliens = aliens ** 2
    print("there are", aliens, "aliens now on earth")
    if aliens > 7400000000:
        break
    print()
    print("password hint: the number of things that are attacking us")
    print()
    guess = int(input("quick! please enter the password: "))

if aliens > 7400000000:
    print("nooooo the aliens have outnumbered us all is lost")
else:
    print("hooray! we won the fight and the world is saved!")    