import random 
print("This is a number guessing game")
print("Guess a number between 1 & 10")
aiState = "loop"
if(aiState == "loop"):
    numberInput = input("Input a Number:")
#n = random.randit(1,10)
    randomList = random.sample(range(1,10), 1)
    if(numberInput == randomList):
        print("Well done! You guessed the correct number")
    else:
        print("The number you guessed was wrong :( Try again to guess the correct number")
        aiState = "loop"
    