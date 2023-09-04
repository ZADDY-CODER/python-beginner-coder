#Ogochukwu Amaeze
#16/12/22
#program uses a function to find unique number in two list of randomly generated number from 0 to 100

import random

def unique(list_1,list_2,n_same): 
  for i in range(0,10):
    #use for loop to apeend numbers to a list
    list_1.append(random.randint(0,100))
    list_2.append(random.randint(0,100))
  #checks for numbers of list_1 in list_2 and append unique number to a new list
  for i in list_1:
    if i not in list_2:
     n_same.append(i)
  #checks number of list_2 in list_1 and appends unique numbers to a new list
  for i in list_2:
    if i not in list_1:
      n_same.append(i)
  return n_same

list_first=[]
list_next=[]
not_same=[]

#print ou results
print("numbers that are not the same in both of the list:",unique(list_first,list_next,not_same))