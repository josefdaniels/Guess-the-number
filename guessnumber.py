import random
import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

max_chances = 0
chances = 5
score = 0
game = random.randint(1, 10)

while True:
	try:
		clear_screen()

		print("GUESS THE NUMBER\n")
		print(f"Your attempts: {chances}")
		print(f"Your score: {score}\n")
		
		number = int(input("Tell me a Number: "))
		chances -= 1
		
		if chances == max_chances:
			print("\nYou've used all your attempts!")
			play_again = input("\nPlay again(y/n): ")
			if play_again == "y":
				chances += 5
				continue
			else:
				break
				
		if number == game:
			print("\nYou got it right!")
			chances += 3
			score += 1
			game = random.randint(1, 10)
			
		elif number > game:
			print("\nThe number you guessed is too high")
		elif number < game:
			print("\nThe number you guessed is too low")
			
		input("\nPress space to continue: ")
		
	except ValueError:
		print("\nEnter number only")
		input("\nPress space to continue: ")