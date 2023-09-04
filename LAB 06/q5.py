#Ogochukwu Amaeze
#16/12/22
#program will use a function to return back the multple and remainer of two numbers

def remainder(num1,num2):
  divide = num1//num2 #to get the whole number of the time num2 will divide into num1
  remain=num1-(divide*num2)#used formulae to calculate remainer
  return divide and remain#return both times of whole number division and remainer

#User can type in number to test if function works (i already test it)
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
print(x//y)
print(remainder(x,y))#prints out return comnand