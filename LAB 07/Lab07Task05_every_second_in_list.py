#Ogochukwu Amaeze
#18/11/22
# this program will find name a new list of the second positions of the old list
import random

def listings(list):
  list=[]
  counter = 0
  
  #Generated 10 random floats
  while counter<10:
    list.append(random.randint(1.0,100.0))
    counter+=1
  print("orginal list:",list)
  
  #Used a while loop to make a new list of the old list even positions
  even_counter=0
  even_position=[]
  while even_counter < 10:
    even_position.append(list[even_counter])
    even_counter+=2

  return even_position
  
even_position=listings(list)
print("list of second positions in original list",even_position)