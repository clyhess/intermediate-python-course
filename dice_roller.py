#dice roll machine

def main ():
#random import variable 
	import random
	
#number of dice rolled
	dice_rolls = 2
#creating a sum of die
	dice_sum = 0  
	for i in range (0, dice_rolls):
#roll ------ variables
		roll = random.randint(1,6)
#create sum
		dice_sum = dice_sum + roll
#print result of roll function
		print(f'You rolled a {roll}')
	print(f'You have rolled a total of {dice_sum}') 
if __name__== "__main__":
  main()