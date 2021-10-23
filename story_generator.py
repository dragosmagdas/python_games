import random

woman = ["a scientist", "a queen", "a pirate", "a giant rabbit"]
man = ["a police oficer", "an artist", "your grandfather", "a robot"]
place = ["on pluto", "at the supermarket", "on a mountain"]
sheWore = ["scuba diving gear", "fairy wings", "a paper bag"]
heWore = ["a purple suit", "a shark costume", "a beach towel"] 
womanSays = ["who are you?", "how many beans make five?", "why?"]
manSays = ["beep boop", "do not eat frogs", "what time you call this?"]
consequence = ["world peace", "chaos", "a giant foot squashed them", "rainbow"]
worldSays = ["nonsense", "cheese is trending now", "i am melting"]
run_game = True
while run_game:
    print(random.choice(woman), "met", random.choice(man), random.choice(place))
    print("she was wearing", random.choice(sheWore))
    print("he was wearing", random.choice(heWore))
    print("she said", random.choice(womanSays))
    print("he said", random.choice(manSays))
    print("the consequence was", random.choice(consequence))
    print("the world said", random.choice(worldSays))
    print()
    stop = input("press enter to play again, S to stop the game")
    print()
    if stop == "S":
        print("Stopping the game, bye bye!")
        run_game = False
