from random import randint

for i in range(1,6):
    GuessNumber = int(input("Enter your GuessNumber from 1 to 5 : "))
    RandomNumber = randint(1,5)
    if RandomNumber == GuessNumber:
        print("You have won the game  -- o -- ")
    else :
        print("You have lost the game,Please try again")
        print("The random number was : ",RandomNumber)
