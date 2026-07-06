import random
import os

score = 0


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print("GUESS THE NUMBER - Home Menu\n")
    print("1 - Start Game")
    print("2 - Rules")
    print("3 - Exit")

    return input("\nChoose your option: ")


def difficulty():
    print("\nDifficulties:")
    print("1 - Easy(5 chances / 1-10)")
    print("2 - Medium(10 chances / 1-30 number)")
    print("3 - Hard(20 chances / 1-60)")

    while True:
        option = input("\nSelect difficulty: ")

        if option == "1":
            return 5, random.randint(1, 10)

        elif option == "2":
            return 3, random.randint(1, 50)

        elif option == "3":
            return 1, random.randint(1, 100)

        else:
            print("Invalid option!")


def menu_guess(chances, score):
    clear_screen()
    print("GUESS THE NUMBER\n")
    print(f"Your attempts: {chances}")
    print(f"Your score: {score}\n")



option = menu()

if option == "3":
    exit()

elif option == "2":
    print("\nGuess the hidden number!")
    exit()

elif option == "1":
    chances, game = difficulty()

while True:
    try:
        menu_guess(chances, score)

        number = int(input("Tell me a number: "))

        chances -= 1

        if number == game:
            print("\nYou got it right!")
            score += 1
            chances += 3

            if game <= 10:
                game = random.randint(1, 10)
            elif game <= 50:
                game = random.randint(1, 50)
            else:
                game = random.randint(1, 100)

        elif number > game:
            print("\nToo high!")

        else:
            print("\nToo low!")

        if chances == 0:
            print("\nYou've used all your attempts!")
            break

        input("\nPress Enter to continue")

    except ValueError:
        print("\nEnter numbers only")
        input("\nPress Enter to continue")
