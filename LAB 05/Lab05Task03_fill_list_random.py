#Ogochukwu Amaeze
#28/10/22

#code1
import random
print("Generating a list of random numbers...")
my_list = []
nums = int(input("How many elements do you want?: "))
x=0
while x<nums:
  my_list.append(random.randint(0,10))
  x+=1
print(my_list)
