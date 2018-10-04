#printing the output of rps
import random
while(True):
	rohan=input("enter r,p,s : ")


	a={1:'r',2:'p',3:'s'}
	c=a[random.randint(1,3)]
	print("u choose ",rohan,"computer a choose",c)
	if(rohan=='r' or rohan=='p' or 	rohan=='s'):
		if(rohan==c):
			print("tie")
		elif((rohan=="r" and c=="p" ) or (rohan=="s" and c=="p") or (rohan=="r" and c=="s")):
			print("ROHAN WINS")
		else:
			print("computer wins")
	else:
			print("enter a proper value : ")
	T=input("enter q to exit")

	if(T=='q'):
		exit()


