#Ogochukwu Amaeze
#30/10/22

#code1
x=1
check = 1
up = 0
down = 9
palindrome = 0

list = []
zero = int(input("Choose a number for your list: "))
list.append(zero)

while x <= 9:
  index_input = int(input("choose another: "))
  list.append(index_input)
  x+=1
print(list)

while check <= 5:
  if list[up] == list[down]:
    up+=1
    down-=1
    check+=1
    palindrome+=1
  else:
    up+=1
    down-=1
    check+=1

if palindrome == 5:
  print("palindrome")

else:
  print("not a palindrome")