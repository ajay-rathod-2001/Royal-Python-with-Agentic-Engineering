import random

print("======== 🏷️💞 Wel-Come to the NUmber Guessing Game 💞🏷️ ========")

while True:
    secrets_num = random.randint(0, 100)
    for i in range(0,5):
        print(f"Attempts {i+1} of 5")

        user_guess_num = int(input("Enter the Guess NUmber [0-9]: "))
        if user_guess_num == secrets_num:
            print(f"Congratulation...💥❤️‍🔥!. You win the guess number game in {i+1} attempts.")
            break
        if user_guess_num > secrets_num:
            print("Too High Number...⚡!. Try it again")
        elif user_guess_num < secrets_num:
            print("Too Low Number...⚡!. Try it again")

        print("------------------------------------------")

    print("The secret number was: ", secrets_num)

    print("="*55)

    user_input = input("Do you play it again..!(yes/no): ")
    if user_input == "no":
        break