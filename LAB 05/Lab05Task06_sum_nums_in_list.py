#Ogochukwu Amaeze
#28/10/22

#code1
import random
my_list = []
x=0
while x<= random.randint(0,10):
  my_list.append(random.randint(0,10))
  x+=1
print(my_list)


travel_check=0
while travel_check<len(my_list):
  sum=my_list[travel_check]
  travel_check+=1
  if travel_check < 1:
    sum=my_list[travel_check]+sum
print(sum)  