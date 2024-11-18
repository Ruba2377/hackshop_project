import random
number=random.randint(1,10)
for x in range(3):
    guess=int(input("Take a guess from 1 to 10:"))
if guess==number:
    print("you won!!")
    break
elif guess>number:
    print("Try lower!!")
elif guess<number:
    print("Try Higher!!")
else:
    print("You Lost!!!")
