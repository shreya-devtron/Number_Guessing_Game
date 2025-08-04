import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

while True:
    try:
        low = int(input("Enter the Lower Bound: "))
        high = int(input("Enter the Upper Bound: "))
        if low >= high:
            print("Error: Upper bound must be greater than lower bound. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter integers only.")

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high) 
ch = 7                        # Total allowed chances
gc = 0                        # Guess counter

while gc < ch:
    gc += 1
    try:
        guess = int(input('Enter your guess: '))
    except ValueError:
        print("Invalid input! Please enter a number.")
        gc -= 1  # Don't count invalid attempts
        continue

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break
    elif guess > num:
        print('Too high! Try a lower number.')
    else:
        print('Too low! Try a higher number.')

if gc >= ch and guess != num:
    print(f'Sorry! The number was {num}. Better luck next time.')
