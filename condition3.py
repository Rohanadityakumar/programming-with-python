#printing the  third condition 
a=int(input("enter your marks:"))
#checking the condition 3
if(a>=90):
	print("A+\nvery good")
elif(a>=80):
	print("A\ngood")
elif(a>=70):
	print("B+\nwork hard")
elif(a>=60):
	print("B\nmust improve")
elif(a>=50):
	print("c+\nreally poor")
elif(a>=40):
	print("c\njust pass has to do a lot of hard work")
else:
	print("STUDENT HAS FAILED\nPLEASE ATTEND REMEDIALS")