#Ogochukwu Amaeze
#28/10/22

#code1
import random
my_list = []
x=0
while x<=9:
  my_list.append(random.randint(0,10))
  x+=1

print(my_list)
index_in_list = 0
j = 9
while (my_list[index_in_list] < my_list[9] or my_list[index_in_list] < my_list[8]):
  index_in_list += 1
  


print("The biggest element in the list is", my_list[index_in_list])
