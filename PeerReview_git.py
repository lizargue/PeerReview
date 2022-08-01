# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Elizabeth White
# Creation Date: 7/31/22
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
#1 print statement not needed
	print()

def chooseCave():
#2 indention error
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
#3 caves instead of cave
	return caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
#4 print statement not needed    
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
#5 missing parenthesis
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
#6 2 equal signs should be used before 'yes' and 'y'
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
#7 chooseCave is defined, whereas choosecave is not    
	caveNumber = choosecave()
	checkCave(caveNumber)
#8 print and input can be combined    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
#9 playAgain=no is not needed for the while loop    
	if playAgain == "no":
#10 print statement needs to come out of loop    
		print("Thanks for planing")

