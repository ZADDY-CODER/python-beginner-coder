#Ogochukwu Amaeze
#18/11/22
# this program allows the user to enter a number and then the program will calculate the sum of the numbers entered and display it


def sum(num1, num2):
  total=num1 + num2
  return total


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("The total of the numbers entered is",sum(num1, num2))