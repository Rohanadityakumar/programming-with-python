#printing tic tac toe game
a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print(a[0],'|',a[1],'|',a[2])
	print("............")
	print(a[3],'|',a[4],'|',a[5])
	print("............")
	print(a[6],'|',a[7],'|',a[8])


p1= True
while True:
	printboard()
	
	if p1:
		p=input("player 1, choose your place :")
		if p in a :
			a[int(p)-1] = 'x'
			p1 = not p1
	else:
		p=input("player 2,choose your place : ")
		if p in a:
			a[int(p)-1] = 'o'
			p1 = not p1
	for i in (0,3,6):
		if(a[i]==a[i+1] and a[i+2]):
			print("sorry!!! game over ")
			exit()

	for i in range(3):
		if(a[i]==a[i+3] and a[i]==a[i+6]):
			print("sorry!!!,game is over")
			if(a[4]=='x'):
				print("congratulation to player 1 ")
			else:
				print("congratulation to player 2 ")
			printboard()
			exit()
	
		
	if(a[0]==a[4] and a[0]==a[8]):
		print("sorry!!!,game is over")
		if (a[4]=='x'):
				print("congratulation to player 1")
		else:
			print("congratulation to player 2")
		printboard()
		exit()
					
	if(a[2]==a[4] and a[2]==a[6]):
		print("sorry!!! game over")
		if(a[4]=='x'):
				print("congratulation to player 1")
		else:
			print("congratulation to player 2")
		printboard()
		exit()
					
