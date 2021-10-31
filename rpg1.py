import random
print("Create your character!")
name = input("what is your character called? ")
age = input("how old is your character? ")
race = input("what is your characters race? ")
print("your characters name is: ", name)
print("your character is ", age, "years old")
print("your characters race is: ", race)
print("-" ,name, ", says lets go on a adventure!")
print()
print("you are in a village") 
print("oh no! some ogres are attacking!")


hero = {
    "hp": 100,
    "attacks": {"aero": 15, "aqua": 30, "fira": 50},
    "name": name,
    "age": age,
    "race": race
}

ogre = {
    "hp": 120,
    "attacks": [{"name": "sword", "dmg": 15}, {"name": "club", "dmg": 30}, {"name": "helmet", "dmg": 50}],
    "name": "Funny Ogre",
    "age": 20,
    "race": "ogre"
}

boss = {
    "hp": 200,
            "attacks": [{"name": "sword", "dmg": 15},
                        {"name": "club", "dmg": 30},
                        {"name": "helmet", "dmg": 50},
                        {"name": "axe", "dmg": 60}
                        ],
            "name": "boss ogre",
            "age": 20,
            "race": "ogre"
            }

fight = True
while fight:
    print("choose an attack to defend the village:")
    print("aero, aqua, or fira")
    attack = input()
    dmg = hero["attacks"][attack]
    ogre["hp"] = ogre["hp"] - dmg
    print("Hitting the {name} with {attack} for {dmg} damage!".format(name=ogre["name"], attack=attack, dmg=dmg))

    if ogre["hp"] <= 0:
        fight = False
        print("We won!")
        print("a dungeon appears!")
        print("you enter it")
        print("inside you find a scroll and read it")
        print("have you ever imagined to pull all your enemies into a big black hole?")
        print("well i have! and now it's posible! with this scroll you can do it!")
        print()
        print("you can now use black hole!")
        hero = {
                "hp": 100,
                "attacks": {"aero": 15, "aqua": 30, "fira": 50 ,"black hole": 10000},
                "name": name,
                "age": age,
                "race": race
                }
        print("you suddenly hear a voice")
        print("GO FROM MY CASTLE!")
        print("you realise you are in a castle")
        print("OR FIGHT!")
        print("CHOOSE GO OR FIGHT!")
        fight_boss = input()
        if fight_boss == "fight":
            fight = True
            while fight:
                print("choose an attack fast!")
                print("aero, aqua, fira, or black hole")
                attack = input()
                dmg = hero["attacks"][attack]
                boss["hp"] = boss["hp"] - dmg
                print("Hitting the {name} with {attack} for {dmg} damage!".format(name=boss["name"], attack=attack, dmg=dmg))
                if boss["hp"] <= 0:
                    fight = False
                    print("the light comes back to the world")
                    print("you win!")
                else:
                    enemy_attack = random.choice(boss["attacks"])
                    hero["hp"] = hero["hp"] - enemy_attack["dmg"]
                    print("the boss ogre attacks you with {name} for {dmg} damage".format(**enemy_attack))
                    if hero["hp"] <= 0:
                        fight = False
                        print("noooo everything is lost")
                        print("you lose")
        elif fight_boss == "go": 
            print("YOU THOUGHT YOU COULD ESCAPE? BOOOOOOOM!")
            print("HA HA HA")
            print("you lose")
    else:   
        enemy_attack = random.choice(ogre["attacks"])
        hero["hp"] = hero["hp"] - enemy_attack["dmg"]
        print("the ogre attacks you with {name} for {dmg} damage".format(**enemy_attack))
        if hero["hp"] <= 0:
            fight = False
            print("We lost!")
