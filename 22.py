#snale and lader
import random
count=0
def myroll():
	return random.randint(1,6)

while(count<=100):
	n=input("press r roll the dice : ")
	if(n=='r'):
		r=random.randint(1,6)
		count=count+r
		print("u got ",r)
		print("new position is",count)

		if(count==8):
			count=37
			print("i got the ladder")
		elif(count==11):
			count(2)
			print("sorry, u got snake")
		elif(count==13):
			count=34
			print("i got the ladder")
		elif(count==25):
			count=4
			print("sorry, u got snake")
		elif(count==38):
			count=9
			print("sorry, u got snake")
		elif(count==40):
			count=70
			print("i got the ladder")
		elif(count==52):
			count=85
			print("i got the ladder")
		elif(count==65):
			count=50
			print("sorry, u got snake")
		elif(count==76):
			count=97
			print("i got the ladder")
		elif(count==89):
			count=79
			print("sorry, u got snake")
		elif(count==93):
			count=83
			print("sorry, u got snake")
		elif(count>=100):
			print("CONGRATULATIONS!!!, U HAVE WON THE GAME")
			exit()

