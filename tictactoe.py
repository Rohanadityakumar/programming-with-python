#printing tic tac toe game
a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print(a[0],'|',a[1],'|',a[2])
	print("............")
	print(a[3],'|',a[4],'|',a[5])
	print("............")
	print(a[6],'|',a[7],'|',a[8])


ROHANITSYOURTURN = True
while True:
	printboard()
	p=input("choose an available space : ")
	if(p in a):
		if(a[int(p)-1]=='x' or a[int(p)-1]=='o'):
			print("place taken, choose another place....")
			continue
			
		else:
			if ROHANITSYOURTURN:
				print("player 1>>")
				a[int(p)+1]=='x'
				ROHANITSYOURTURN = not ROHANITSYOURTURN
			
		
			else:
				print("player 2>>")
				a[int(p)-1] = 'o'
				ROHANITSYOURTURN = not ROHANITSYOURTURN
