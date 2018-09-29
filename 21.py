#printing random function
import random

while True:
	i=input("enter 'r' to roll 'q to quit : ")
	if(i=='q'):
		print("THANK YOU FOR PLAYING")
		exit()


	if(i=='r'):
		print ("you got",random.randint(1,6))