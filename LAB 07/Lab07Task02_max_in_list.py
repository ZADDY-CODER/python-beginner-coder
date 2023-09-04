#Ogochukwu Amaeze
#18/11/22
#this program will find the max number in a list

import random

def list(list):
  list=[]
  counter = 0
  
  #Generated 10 random numbers
  while counter<10:
    list.append(random.randint(1.0,100.0))
    counter+=1
  print(list)
  return list

def max_list(list):
  max_value = list[0]
  for i in range(1,len(list)):
    if list[i] > max_value:
      max_value = list[i]
  return max_value

list = list(list)
print("\nthe maximum value in the list is",max_list(list),"\n")

#code2,Found out a shorter way but unsure if it would qualify as an answer
def list(list):
  list=[]
  counter = 0
  
  #Generated 10 random numbers
  while counter<10:
    list.append(random.randint(1.0,100.0))
    counter+=1
  print(list)
  return list

def max_list(value):
  list.sort()
  max_value = list[len(list)-1]
  return max_value

list = list(list)

print("\nthe maximum value in the list is",max_list(list))