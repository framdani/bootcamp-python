import random

number = random.randint(1, 99)
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
x = input("What's your guess between 1 and 99?\n")
attempt=0
while (1):
    attempt=attempt+1
    if x=='exit':
        print("Goodbye!")
        break
    elif x.isdigit()==False:
        print("That's not a number.")
    elif int(x) == number:
        if number == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if attempt == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in {} attempts!".format(attempt))
        break
    elif int(x)<number:
        print("Too low!")
    elif int(x)>number:
        print("Too high!")
    x = input("What's your guess between 1 and 99?\n")

