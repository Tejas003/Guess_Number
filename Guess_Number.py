#Program that Picks up a Random number between a User specified range and Asks User to Guess the same

#importing Random Libray 
import random
#importing Time Library
import time

Rand = None
Hint = 0
Chances = 6

#Function to print an exit message and end the Game if User entered No
def EndGame(Openion) :
	if Openion == 'No' :
		print('\n\n******************************************************\nYou have succesfully exited from the Game\n******************************************************\n')
		quit();

#Function to provide Hint based on the occurance of Hint like 1st, 2nd or 3rd
def HintCal(No) :
	#If its a second hint it specifies whether the Random number is Bigger, Smaller or Near the center of the range
	if Hint == 2 :   
		mid = int((Lowest+Largest)/2)
		if Rand > mid :
			print('\n===================================================\nHINT: My Number is Bigger than the Midrange\n===================================================\n')
		elif Rand > mid :
			print('\n===================================================\nHINT: My Number is Smaller than the Midrange\n===================================================\n')
		else :
			print('\n===================================================\nHINT: My Number is Near the the Midrange\n===================================================\n')
	#If its a third hint it specifies the lst Digit of the number		
	elif Hint == 3 :   
		last = Rand%10
		print('\n===================================================\nHINT: Last Digit of My number is',last,'\n===================================================\n')
		print('\n\n******************************************************\nYou have used all your Hints kindly Continue Guessing******************************************************\n')
	
	#If its a first hint it specifies whether the Random number is Even or Odd 						
	else :
		if Rand%2 == 0 :
			print('\n===================================================\nHINT: My Number is an Even Number\n===================================================\n')
		else :
			print('\n===================================================\nHINT: My Number is an Odd Number\n===================================================\n')
			

#The Program welcomes the User
Name = input("Dear Friend, May I know your Name?\n")
print('\nHello',Name,)
Play = input("\nWould you like to play the Game?\nNote: Type 'Enter' to Play and 'No' to quit\n")

EndGame(Play)

print("\n===================================================\nNote: Kindly Go through all the Rules of this Game !!!\n1. You select the range of numbers for me to choose from(Note that the range should be >=50)\n2. Once I pick a number you get 6 Chances to Guess the number\n3. You get three Hints(Note that each Hint you use kills one of your Chances!)\n===================================================\n")

print("\nDear "+Name+", Please specify the range in which you would like me to pick the number")

#While loop will keep asking the values in the Range until those meet the requirement
#It will also ask if you want to quit
while(Rand == None) :
	#Try Catch block to avoid non numeric values
	try:
		#Type conversion to Int in case number entered is float it will truncate the decimal part
		Lowest = int(input('\nPlease type the loweset number from your choice of range\n'))
		Largest = int(input('\nPlease type the largest number from your choice of range\n'))

	except:
		print('\n******************************************************\nKindly enter numeric value and Try Again!!\n')
		EndGame()

	#randint(range) uses random library and picks a random number from the given range
	#other functions are random.random() - This lists random number between 0.0 and 0.1 
	# random.choice(list) it picks random item or number from given list
	if Largest < Lowest :
		print("\nPlease enter Valid Range\n<Largest number is Smaller than the Lowest>")
		Play = input("\nWould you like to continue Guessing?\nNote: Type 'Enter' to Continue and 'No' to quit\n")


	elif (Largest - Lowest) >=50:

		Rand = random.randint(Lowest,Largest)

		print('\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'+Name+', Be ready I am Picking a number from your Range\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
		for countdown in range(5) :
			print(countdown,' ')
			time.sleep(1)
		print('\n')

	else :
		print("\nPlease enter Valid Range\n<The Range is not greater than or equal to 50>")
		Play = input("\nWould you like to continue Guessing?\nNote: Type 'Enter' to Continue and 'No' to quit\n")

	
print(Name+' I have Picked a number!!! Start Guessing\n')

while (Chances>0):
	print('\n===================================================\n<You have ',Chances,' Chances and have used',Hint,' Hints>\n')
	
	try:
		Guessed = int(input('\n--------------------------------------------------\nWhats your Guess?\n>'))
	except:
		print('You have entered an Invalid Number!!!!!\nThus you have also missed a chance\n')
		Chances = Chances - 1
		continue

	if Guessed == Rand :
		print('\n################################################\nBingo!! You have Guessed it right !! It was ',Guessed,'\n')
		print('You have used ',Chances,' Chances and ',Hint,' Hints\nTotal = Chances + Hints = ',Chances,' + ',Hint,' =',(Chances+Hint),'\n################################################\n')
		break

	else :
		if Guessed > Rand :
			print('Sorry you missed it!! You are going Hight!!\n--------------------------------------------------\n')
		else :
			print('Sorry you missed it!! You are going low!!\n--------------------------------------------------\n')

		Play = input("\nWould you like to continue Guessing?\nNote: Type 'Enter' to Continue and 'No' to quit\n")


		
		while(Hint < 3):
			Hints = input("If you want to use a Hint Press 'Yes' Otherwise Press 'Enter' to continue Guessing\n")
			if Hints == 'Yes' :
				pass
			else :
				break

			Hint = Hint + 1

			#Calling or Invoking HintCal()
			HintCal(Hint)
			


			

	Chances = Chances - 1
	#Invoking EndGame() Function
	EndGame(Play)
		

