answer = 7

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == answer:
        print("Correct! You found it.")
        break
    elif guess < answer:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")