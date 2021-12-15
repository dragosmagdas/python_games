
import time

def stay():           
    print(" (. .) ")
    print("   | ")
    print("   | ")
    print("   | ")
    print(" \ | / " )
    print("  \|/ " )
    print("  / \ ")
    print(" /   \ ")
    print("/     \ ")
    

def walk():
    print(" (. .) ")
    print("   | ")
    print("   | ")
    print("   | ")
    print(" \ | / " )
    print("  \|/ " )
    print("  / \__ ")
    print(" /     \ ")
    print("/       \ ")

stay_on = True
while True:
    if not stay_on:
        walk()
    else:
        stay()

    stay_on = not stay_on
    time.sleep(0.3)
    
    