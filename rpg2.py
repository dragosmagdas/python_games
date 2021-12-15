import random
import time

items = {
    "coconut": {
        "name": "coconut",
        "healing": 70,
    },
    "heal potion": {
        "name": "heal potion",
        "healing": 50,
    },
    "light stone":{
        "name": "light stone",
        "healing": 70,
    }
}
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
        "special_attack": {
            "name": "slop",
            "dmg": 15
        } 
    },
    "skeleton": {
        "weapon": "sword",
        "dmg": 20,
        "sp": 80,
        "hp": 30,
        "special_attack": {
            "name": "dark slash",
            "dmg": 20
        }
    },
    "troll": {
        "weapon": "club",
        "dmg": 30,
        "sp": 90,
        "hp": 50,
        "special_attack": {
            "name": "bash", 
            "dmg": 25
        }
    }
}

levels = {
    "island": {
        "enemies": ["slime"],
        "items": ["coconut", "heal potion"],
        "boss": {
            "name": "king slime",
            "weapon": "none",
            "dmg": 20,
            "sp": 70,
            "hp": 30,
            "is_boss": True,
            "special_attack": {
                "name": "sloper",
                "dmg": 30
            }
        }
    },
    "cave": {
        "enemies": ["slime", "skeleton"],
        "items": ["light stone", "heal potion"],
        "boss": {
            "name": "king skeleton",
            "weapon": "sword",
            "dmg": 30,
            "sp": 90,
            "hp": 40,
            "is_boss": True,
            "special_attack": {
                "name": "darker slash",
                "dmg" : 40
            }
        }

    },
    "castle": {
        "enemies": ["slime", "skeleton", "troll"],
        "items": ["heal potion"],
        "boss": {
            "name": "dark king",
            "weapon": "magic",
            "dmg": 40,
            "sp": 90,
            "hp": 50,
            "is_boss": True,
            "special_attack": {
                "name": "BOOM",
                "dmg" : 50                
            }
        }
    }
}


print("Create your character!")
name = input("what is your character called? \n")
age = input("how old is your character? \n")
clazz = input("what is your characters class? Choose from: {available_classes} \n".format(available_classes=list(classes.keys())))
print("="*20)

print("your characters name is: ", name)
print("your character is ", age, "years old")
print("your characters class is: ", clazz)
print("-",name, "let's go on an adventure!")
time.sleep(random.randint(1,10))
print("="*20)

def spawn_enemy(level):
    enemy_to_spawn = random.choice(level["enemies"])
    print("oh no! you encountered a {enemy}".format(enemy=enemy_to_spawn))
    enemy = dict(enemy_classes[enemy_to_spawn])
    enemy.update({"name": enemy_to_spawn, "is_boss": False})
    return enemy

def spawn_boss(level):
    boss_to_spawn = level["boss"]
    print("oh no! you encountered a {boss}".format(boss=boss_to_spawn["name"]))
    boss = dict(level["boss"])
    return boss

def spawn_item(level):
    item_to_spawn = random.choice(level["items"])
    print("nice! we found a {item}".format(item=item_to_spawn))
    item = dict(items[item_to_spawn])
    return item

def player_attack(player, enemy):
    if len(player["items"]) > 0:
        choice = input("you have the following items {names}, do you want to use any of them? (y/n) \n".format(names=player["items"]))
        if choice == "y":
            # use item
            item_name = input("enter the name of the item you want to use \n")
            item = dict(items[item_name])
            player["items"].remove(item)
            player["hp"] = player["hp"] + item["healing"]
    if player["sp"] >= player["special_attack"]["dmg"]:
        choice = input("you have {hp} health and {sp} sp, do you want to do a special attack? (y/n) \n".format(sp=player["sp"], hp=player["hp"]))
        if choice == "y":
            # special attack
            special_hero_attack(player, enemy)
        else:
            regular_hero_attack(player, enemy)
    else:
        print("special attack no longer available, doing a normal attack")
        regular_hero_attack(player, enemy)     
            
def regular_hero_attack(player, enemy):
    dmg = player["dmg"]
    enemy["hp"] = enemy["hp"] - dmg
    print("Hitting the {name} with a regular attack for {dmg} damage!".format(name=enemy["name"], dmg=dmg))

def special_hero_attack(player, enemy):
    attack_name = player["special_attack"]["name"]
    dmg = player["special_attack"]["dmg"]
    enemy["hp"] = enemy["hp"] - dmg
    player["sp"] = player["sp"] - dmg
    print("Hitting the {name} with a {attack} attack for {dmg} damage!".format(name=enemy["name"], dmg=dmg, attack=attack_name))

def enemy_attack(player, enemy):
    dmg = enemy["special_attack"]["dmg"]
    if enemy["sp"] >= dmg:
        choice = random.randint(1, 2)
        if choice == 1:
            special_enemy_attack(player, enemy)
        else:
            regular_enemy_attack(player, enemy)
    else:
        regular_enemy_attack(player, enemy)

def special_enemy_attack(player, enemy):
    attack_name = enemy["special_attack"]["name"]
    dmg = enemy["special_attack"]["dmg"]
    player["hp"] = player["hp"] - dmg
    enemy["sp"] = enemy["sp"] - dmg
    print("the {enemy} hits you with a {skill} for {dmg} dmg".format(enemy=enemy["name"], skill=attack_name, dmg=dmg))

def regular_enemy_attack(player, enemy):
    dmg = enemy["dmg"]
    player["hp"] = player["hp"] - dmg
    print("the {enemy} hits you with a regular attack for {dmg} dmg!".format(enemy=enemy["name"], dmg=dmg))

def next_level(level_name):
    if level_name == "island":
        return "cave"
    elif level_name == "cave":
        return "castle"
    else:
        return None

hero = {
    "name": name,
    "age": age,
    "class": clazz,
    "hp": 100,
    "items": []
}
hero.update(classes[clazz])

playing = True
monsters_beaten = 0
SPAWN_MONSTER = 1
SPAWN_ITEM = 2
MONSTERS_TO_FIGHT_BEFORE_BOSS = 10
current_level = "island"
current_enemy = None

print("you are on an island explore it!")
while playing:
    time.sleep(random.randint(1,10))
    level = levels[current_level]
    print("="*20)
    if not current_enemy:
        if monsters_beaten == MONSTERS_TO_FIGHT_BEFORE_BOSS:
            time.sleep(random.randint(1,10))
            current_enemy = spawn_boss(level)
        else:
            choice = random.randint(1, 2)
            if choice == SPAWN_MONSTER:
                current_enemy = spawn_enemy(level)
            elif choice == SPAWN_ITEM:
                item = spawn_item(level)
                hero["items"].append(item)
    else:
        print("you are fighting with a {enemy}".format(enemy=current_enemy["name"]))
        # fight
        player_attack(hero, current_enemy)
        if current_enemy["hp"] <= 0:
            print("{name} defeated".format(name=current_enemy["name"]))
            if current_enemy["is_boss"] == True:
                monsters_beaten = 0
                next = next_level(current_level)
                if not next:
                    print("You won the game!")
                    playing = False
                else:
                    print("You completed {current} level, moving to {next}".format(current=current_level, next=next))
                    current_level = next
            else:
                monsters_beaten = monsters_beaten + 1
            current_enemy = None
        else:
            time.sleep(3)
            print()
            enemy_attack(hero, current_enemy)
        if hero["hp"] <= 0:
            print("You lost!")
            current_enemy = None
            playing = False