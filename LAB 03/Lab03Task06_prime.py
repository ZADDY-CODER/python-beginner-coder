#Ogochukwu Amaeze
#17/10/2022

print("Guess a number game!")
x = int(input("Enter a number: 0 - 10: "))
while x > 5:
  print("too high - try again")
  x = int(input("Enter a number: 0 - 10: "))

while x < 5:
  print("too low - try again")
  x = int(input("Enter a number: 0 - 10:"))

while x == 5:
  print("well done!")
  if x == 5:
    break