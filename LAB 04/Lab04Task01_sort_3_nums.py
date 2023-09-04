#Ogochukwu Amaeze
#21/10/22

#code 1
print("A program to sort 3 numbers")
num_1 = int(input("enter a number: "))
num_2 = int(input("...and another: "))
num_3 = int(input("...and another: "))

if num_2 < num_1 > num_3 and num_2 > num_3:
  print ("\nSorted in ascending order...\n",num_3,num_2,num_1,)
elif num_3 > num_2 and num_1 > num_3:
 print("\nSorted in ascending order...\n",num_2,num_3,num_1)
  
elif num_1 < num_2 > num_3 and num_1 > num_3:
 print("\nSorted in ascending order...\n", num_3,num_1,num_2)
  
elif num_3 > num_1 and num_2>num_3:
 print("\nSorted in ascending order...\n",num_1,num_3,num_2)

elif num_2 < num_3 > num_1 and num_1 > num_2:
  print("\nSorted in ascending order...\n", num_2,num_1,num_3)
elif num_2>num_1 and num_3>num_2:
 print("\nSorted in ascending order...\n",num_1,num_2,num_3) 