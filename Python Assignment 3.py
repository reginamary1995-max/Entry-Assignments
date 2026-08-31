# 1. ************************ Number Guessing Game
import random
secret_number = random.randint(1, 10)
attempts = 3
while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    if guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

    attempts -= 1

else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)

# 2.**************************  Multiplication Table Generator
number = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

# 3. ***********************BMI Calculator

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your BMI is:", format(bmi, ".2f"))