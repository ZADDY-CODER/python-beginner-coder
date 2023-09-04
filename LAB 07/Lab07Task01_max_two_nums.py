#Ogochukwu Amaeze
#18/11/22

#this program will allow the user to input two numbers and print out the max of the two numbers

def max(num1, num2):
  if num1 > num2:
    return num1
  else: 
    return num2

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
    
print( "max",(num1,num2), "returned: ", max(num1,num2))