#Ogochukw Amaeze
#14\10\2022

#code 1
neg = int(input("Enter a number to see a count from zero: "))

while neg < 1:
 neg = int(input("!Enter a positive number only:! "))

if neg > 0:
  print("You entered:", neg)

print("Counting from zero...")
while neg >= neg :
  print(neg,end=" ")
  neg = neg - 1
  if neg == -1:
   break



#code 2
print("\n")
neg = int(input("\nEnter a number to see a count from zero: "))

while neg < 1:
 neg = int(input("!Enter a positive number only:! "))

if neg > 0:
  print("You entered:", neg)

print("Counting from zero...")

for x in range(0,neg+1):
  print(x, end=" ")
    