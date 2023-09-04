#Ogochukwu Amaeze
#25/11/2022
# this program takes a book of intergers and prints out the sum of the numbers
int_book= open("integers_example.txt", "r")
int_list = list(int_book)



def sum_of_integers(int_list):
  int_turn_list=0
  total = 0
  while int_turn_list<len(int_list):
    first_nums=list(int_list[int_turn_list].split())
    travel=0  
    while travel<len(first_nums):
      total += int(first_nums[travel])
      travel+=1
    int_turn_list+=1
    
  return total

print("reading file:  integers_example.txt\nsum of integers:",sum_of_integers(int_list))

