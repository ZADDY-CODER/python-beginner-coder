#Ogochukwu Amaeze
#17/10/22

x = int(input("Enter a num greater than 1: "))
while x<=1:
 x = int(input("Enter a num greater than 1: "))


print("Check prime:",x)
if x >= 8:
 if ((x == 2) or (x%2 == 1)) and (x%3 != 0) and (x%5 != 0) and (x%7 !=0):
  print("prime")
 else:
  print("not prime")

if x < 8:
  if (x==2) or (x%2 == 1):
   print("prime")
  else:
   print("not prime")