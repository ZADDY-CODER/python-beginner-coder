#Ogochukwu Amaeze
#21/10/2022

#code 1
print("***Greatest Common Denominator (GCD) Calculator***")

num_1 = int(input("Enter first number: "))
while num_1<1:
  num_1 =int(input("ENTER A POSTIVE WHOLE NUMBER: PLEASE"))
  
num_2 = int(input("Enter other number: "))

while num_2<1:
  num_2=int(input("ENTER A POSTIVE WHOLE NUMBER: PLEASE"))
x=1
if num_1==num_2:
 print("GCD is",num_1)

while num_1>num_2:
  lcm = num_2*x
  x+=1

  if lcm%num_1==0:
    break
    
while num_1<num_2:
   lcm = num_1*x
   x+=1

   if lcm%num_2==0:
    break
    
if num_1>num_2 or num_2>num_1:
  print("GCD is:",int(num_1*num_2/lcm))
