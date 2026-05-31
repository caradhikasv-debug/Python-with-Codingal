import random
playing=True
num=random.randint(0, 9)
print("i will generate a random number from 0 to 9")
print("you have to guess the number one at time")
print("the game will end when you get it right")
while playing:
    gu=int(input("Give me your best guess:"))
    if num==gu:
        print("you win the game")
        print("the number was",num)
        break
    else:
        print("Your guess is not right try again ")