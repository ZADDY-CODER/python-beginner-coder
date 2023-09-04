#Ogochukwu Amaeze
#28/10/22

#code1

import random

x=0
my_list = []
while x<= random.randint(0,10):
  my_list.append(random.randint(0,10))
  x+=1
print(my_list)

odd_found=0
num_of_list = len(my_list)
travel_check = 0


while travel_check < num_of_list:
  if my_list[travel_check]%2!=0:
    odd_found+=1
  travel_check+=1

print("\n",odd_found,"odd numbers found")