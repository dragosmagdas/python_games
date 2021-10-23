powers = {
    "epic zero": "meta manipulator",
    "glory girl": "flight", 
    "captain justice": "super strength",
    "selfie": "magic",
    "dog gone": "meta morph",
    }

run = True
while run:
    print("Search in the hero database, type EXIT to stop")
    name = input()
    if name == "EXIT":
        print("bye bye")
        run = False
    else:
        if name in powers:
            print("Hero found:", name, "power:", powers[name])
        else:
            print("hero not in database")
