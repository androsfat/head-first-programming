from random import randint
secret = randint(1, 10) # Create a random number
print("Welcome!")
guess = 0 # Initialise a false value to make the loop run
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("You win!")
    else: 
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
print("Game Over!")
