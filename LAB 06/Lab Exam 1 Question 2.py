#Ogochukwu Amaeze
#Question 2
#11/11/22

import random
list=[]
counter = 0
number_checker=1
index_counter=0
list_operater=0
#Generated 10 random floats
while counter<10:
  list.append(random.randint(1,20))
  counter+=1
print("The list is:",list)

#Sort list in numerial order
list.sort()

while list_operater<len(list):
  if number_checker==list[index_counter]:
    print(number_checker,"is in the list")
    index_counter+=1
    number_checker=1
    list_operater+=1
  else:
    number_checker+=1