#using function
x=int(input("enter a number))
y=int(input("enter another number))
O=input("what do u want me to do ROHAN??? is it +,-,*,/")
            
#using add function
def add():
       return x+y
        
#using sub function
def sub():
       return x-y

#using multi function
def multi():
        return x*y
 
#using div function
def div():
      return x/y

if(o=='+'):
        res=add()
            
elif(o=='-'):
          res=sub(X,Y)

elif(o=='*'):
           res==multi(x,y)
     
elif(o=='/'):
           res==div(x,y)
            
print(res)
