import random
import time

classes = {
    "magician": {
        "weapon": "Simple Magician Staff",
        "dmg": 5,
        "sp": 100,
        "special_attack": {
            "name": "fireball",
            "dmg": 20
        }
    },
    "warrior": {
        "weapon": "Long sword",
        "dmg": 15,
        "sp": 100,
        "special_attack": {
            "name": "cleave",
            "dmg": 25
        }
    },
    "dragon knight": {
        "weapon": "Dragon's Bane",
        "dmg": 20,
        "sp": 100,
        "special_attack": {
            "name": "dragon hit",
            "dmg": 30
        }
    }
}

enemy_classes = {
    "slime": {
        "weapon": "none",
        "dmg": 10,
        "sp": 70,
        "hp": 20,
        "special_attacks": {
            "slop": 15
        } 
    },
    "skeleton": {
        "weapon": "sword",
        "dmg": 20,
        "sp": 80,
        "hp": 30,
        "special_attacks": {
            "dark slash": 20
        }
    },
    "troll": {
        "weapon": "club",
        "dmg": 30,
        "sp": 90,
        "hp": 50,
        "special_attacks": {
            "bash": 25
        }
    }
}

levels = {
    "island": {
        "enemies": ["slime"],
        "items": ["coconut", "heal potion"],
        "king slime": {
            "weapon": "none",
            "dmg": 20,
            "sp": 70,
            "hp": 30,
            "special_attacks": {
                "sloper": 30
            }
        }
    },
    "cave": {
        "enemies": ["slime", "skeleton"],
        "items": ["light stone", "heal potion"],
        "king skeleton": {
            "weapon": "sword",
            "dmg": 30,
            "sp": 90,
            "hp": 40,
            "special_attacks": {
                "darker slash": 40
            }
        }

    },
    "castle": {
        "enemies": ["slime", "skeleton", "troll"],
        "items": ["heal potion"],
        "the dark king": {
            "weapon": "magic",
            "dmg": 40,
            "sp": 90,
            "hp": 50,
            "special_attacks": {
                "BOOM": 50                
            }
        }
    }
}


print("Create your character!")
name = input("what is your character called? \n")
age = input("how old is your character? \n")
clazz = input("what is your characters class? Choose from: {available_classes} \n".format(available_classes=list(classes.keys())))
print()

hero = {
    "name": name,
    "age": age,
    "class": clazz,
    "hp": 100,
    "items": []
}
hero.update(classes[clazz])

print("your characters name is: ", name)
print("your character is ", age, "years old")
print("your characters class is: ", clazz)
print("-",name, "let's go on an adventure!")
time.sleep(2)
print()

on_island = True
monsters_beaten = 0
SPAWN_MONSTER = 1
SPAWN_ITEM = 2
current_level = None
current_enemy = None

def spawn_enemy(level):
    enemy_to_spawn = random.choice(level["enemies"])
    print("oh no! you encountered a {enemy}".format(enemy=enemy_to_spawn))
    enemy = dict(enemy_classes[enemy_to_spawn])
    enemy.update({"name": enemy_to_spawn})
    return enemy

def spawn_item(level):
    item_to_spawn = random.choice(level["items"])
    print("nice! we found a {item}".format(item=item_to_spawn))
    return item_to_spawn

def regular_hero_attack(player, enemy):
    dmg = player["dmg"]
    enemy["hp"] = enemy["hp"] - dmg
    print("Hitting the {name} with a regular attack for {dmg} damage!".format(name=enemy["name"], dmg=dmg))

def special_hero_attack(player, enemy):
    attack_name = player["special_attack"]["name"]
    dmg = player["special_attack"]["dmg"]
    enemy["hp"] = enemy["hp"] - dmg
    hero["sp"] = hero["sp"] - dmg
    print("Hitting the {name} with a {attack} attack for {dmg} damage!".format(name=enemy["name"], dmg=dmg, attack=attack_name))

print("you are on an island explore it!")
current_level = "island"
while on_island:
    time.sleep(random.randint(0,1))
    level = levels[current_level]
    print("DEBUG:", hero, current_enemy, current_level, monsters_beaten)
    print()
    if not current_enemy:
        choice = random.randint(1, 2)
        if choice == SPAWN_MONSTER:
            current_enemy = spawn_enemy(level)
        elif choice == SPAWN_ITEM:
            item = spawn_item(level)
            hero["items"].append(item)
    else:
        print("you are fighting with a: ", current_enemy)
        # fight
        if current_enemy["hp"] <= 0:
            print("{name} defeated".format(name=current_enemy["name"]))
            current_enemy = None
            monsters_beaten = monsters_beaten + 1
        elif hero["hp"] <= 0:
            print("you lost")
            current_enemy = None
            on_island = False
        elif hero["sp"] <=0:
            print("special attack no longer available, doing a normal attack")
            regular_hero_attack(hero, current_enemy)
        else:
            choice = input("you have {sp} sp, do you want to do a special attack? (y/n) \n".format(sp=hero["sp"]))
            if choice == "y":
                # special attack
                special_hero_attack(hero, current_enemy)
            else:
                regular_hero_attack(hero, current_enemy)