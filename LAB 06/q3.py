#Ogochukwu Amaeze
#16/12/22
#program return 10 number from the user in reverse order

#code 1
reverse=[]
count=9
num=(input("Enter a 10 numbers seperated by a space: "))

num = list(num.split())# split and turn nums into a list

while count>=0:# using while loop to reverse num list
  reverse.append(num[count])
  count-=1

print("The reverse of the numbers entered is:"," ".join(reverse))
#end of code 1

print("\n")

#code 2
list=[]
reversed=[]
counter=0
#uses while loop to append users input in to a list
while counter<10:
  num=str(input("Enter a number: "))# turn into a str to be able to join function
  list.append(num)
  counter+=1

while counter>0:#appends reverse order of a list to a new list
  reversed.append(list[counter-1])
  counter-=1
#prin t outs reversed order
print("The reverse of the numbers enter is:"," ".join(reversed))