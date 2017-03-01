from builtins import input
import random

def roll(sides=6):
	num_rolled = random.randint (1, sides)
	return num_rolled
	
def main():
	sides = 12
	rolling = True
	
	while rolling:
		roll_again = input ("Ready to roll? ENTER=Roll. Q=Quit")
		dice_roll = input ("How many times would you like to roll the dice?")
		if roll_again.lower() != "q":
			times_rolled = 0
			while times_rolled < int(dice_roll):
				num_rolled = roll(sides)
				times_rolled = times_rolled + 1
			
				print("You rolled a {}".format( num_rolled))
		else:
			rolling = False
			
	print("Thanks for playing.")

	
main()