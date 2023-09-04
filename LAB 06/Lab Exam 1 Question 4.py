#Ogochukwu Amaeze
#Question 4
#11/11/22

import random
list=[]
counter = 0

#Generated 10 random floats
while counter<10:
  list.append(random.randint(1,9))
  counter+=1
print("Original:",list)

REVERSE=[]
counter=0
index=9
#reversing the orginal list
while counter<10:
  REVERSE.append(list[index])
  counter+=1
  index-=1
print("Reversed:",REVERSE)

#Checking if same at each index
INDEX_UP=0
same = []

while INDEX_UP<10:
  if list[INDEX_UP]==REVERSE[INDEX_UP]:
    same.append(list[INDEX_UP])
    INDEX_UP+=1
  else:
    INDEX_UP+=1
  
# print(same)
x=len(same)-1 #x is the index in the list same
printing=0 # to ensure "SAME ELEMENTS" is only printed once

if x>0:
  if printing==0:
     print("Same elements:") 
     printing+=1
  while x>-1:
    print(same[x],end='\n')
    x-=1

else:
  print("there are no element the same in each list at a given index")