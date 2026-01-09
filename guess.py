import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("🔢 I'm thinking of a number between 1 and 100.")
print("👉 Try to guess it!\n")

while True:
   
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess >= 1 and guess <=100:
            if guess < secret_number:
                print("📉 Too low! Try again.\n")
            elif guess > secret_number:
                print("📈 Too high! Try again.\n")
            else:
                print(f"🎊 Congratulations!")
                print(f"✅ You guessed the number {secret_number} in {attempts} attempts.")
                break
        else :
            print("❌ Invalid input! Please enter a valid number.\n")

