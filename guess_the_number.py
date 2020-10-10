import random

rnumber = random.randrange(0, 101)
guessed = False

while guessed==False :
    try:
        candidate = int(input("I made up a number. Can you guess it? \n"));
        
        if candidate > rnumber :
            print("Too high")
        elif candidate < rnumber :
            print("Too low")
        else :
            guessed = True
            print("Congratulations you won!")        
    except :
        print("Please entere a number \n");