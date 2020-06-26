import random

def compare():
    win = random.randrange(1,10)
    print(win)
    flag = True
    while flag:
        num = int(input("Write a number: "))
        if num > win:
            print("Nope, try lower")
            
        elif num < win:
            print("Nope, try higher")
            
        elif num == win:
            print("nice job")
            flag = False
    
compare()