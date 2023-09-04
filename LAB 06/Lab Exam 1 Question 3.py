#Ogochukwu Amaeze
#Question 2
#11/11/22


#Allow to user to choose numbers in list
x=1
list = []
zero = int(input("Choose a number: "))
list.append(zero)

while x <= 4:
  index_input = int(input("choose another: "))
  list.append(index_input)
  x+=1
print("list is",list)

#Checks for primes in list
primes = []
x=2
not_prime=0

x=2
TRAVEL_INDEX=0
while TRAVEL_INDEX<len(list):
  while x<=list[TRAVEL_INDEX]//2:
    if list[TRAVEL_INDEX]%x==0:
      x+=1
      not_prime+=1
      
    else:
      x+=1
      not_prime==0

  if not_prime==0:
    primes.append(list[TRAVEL_INDEX])
  
  TRAVEL_INDEX+=1
  #unsure why appending stops at a not prime number, but lets assume that it does not

#displays primes to user
print("Primes in list are:",primes)
