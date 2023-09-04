#Ogochukwu Amaeze
#21/10/22

#code1
import random
import math
def estimate_pi(darts):
  radius=1 #circle has radius of 1 unit
  thrown=0 #number of darts thrown
  inside_circle=0
  while thrown<darts:
    x=random.uniform(-radius,radius)
    y=random.uniform(-radius,radius)
    if math.sqrt(x**2+y**2)<=radius:
      inside_circle+=1
    thrown+=1
  pi=(4*inside_circle/thrown)
  return pi

print("***PI Dart-throw Simulator***")
darts=int(input("How many darts?: "))
round=0 #this is for the five times of estimating pi

while darts<darts*10:
  estimate = estimate_pi(darts)
  print("PI is estimated to be...        >>>>\n",estimate)
  round+=1
  darts *= (10)
  if round==5:
    break
  print("How many darts?:",darts)