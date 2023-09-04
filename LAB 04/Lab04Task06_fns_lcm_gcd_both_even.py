#Ogochukwu Amaeze
#21/10/2022

#code1
def lcm(num_1,num_2):
  x=1
  
  while num_1>num_2:
    LCM=num_2*x
    x+=1
    if LCM%num_1==0:
      break
    
  while num_2>num_1:
    LCM=num_1*x
    x+=1
    if LCM%num_2==0:
      break
  return LCM

num_1 = int(input("Enter first number: "))
while num_1<1:
  num_1 =int(input("ENTER A POSTIVE WHOLE NUMBER: PLEASE"))
  
num_2 = int(input("Enter other number: "))

while num_2<1:
  num_2=int(input("ENTER A POSTIVE WHOLE NUMBER: PLEASE"))

LCM=lcm(num_1,num_2)
print("GCD is",int((num_1*num_2)/LCM))
print("LCM is",LCM)

if num_1%2==0 and num_2%2==0:
  print("Both even?:",True)
else:
  print("Both even?:",False)