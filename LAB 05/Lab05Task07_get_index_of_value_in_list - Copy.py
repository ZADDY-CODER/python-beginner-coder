#Ogochukwu Amaeze
#30/10/22

#code 1
my_list = [1, 2, 3, 5, 7, 11, 13, 17]
index = 0
print("***Number Index Finder***")

print(my_list)
choosen = int(input("Enter a number to find its index: "))

if 1>choosen or choosen>17:
  if (choosen != 2 or choosen%2==0) :
    print("Number",choosen,"not found in list: -1")


else:
  while my_list[index] != choosen:
    index+=1
    if index == 8:
      break
  print("Number",choosen,"found at index:",index)