#Ogochukwu Amaeze
#Question 1 
#11/11/22

import random
list=[]
counter = 0

#Generated 10 random floats
while counter<10:
  list.append(random.uniform(1.0,100.0))
  counter+=1
print(list)

#Used a while loop to calculate total in even position
even_counter=0
total_even=0
while even_counter < 10:
  total_even=list[even_counter]+total_even
  even_counter+=2
print("\nTotal of the numbers in the even positions is",total_even)

#Used a while loop to calculate total in odd position
odd_counter=1
total_odd=0
while odd_counter < 10:
  total_odd=list[odd_counter]+total_odd
  odd_counter+=2

print("\nTotal of the numbers in the odd positions is",total_odd)
