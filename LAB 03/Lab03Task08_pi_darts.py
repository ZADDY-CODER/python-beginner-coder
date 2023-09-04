#Ogochukwu Amaeze
#17/10/2022

import random
import math

number_of_points = input("Insert a positive whole number of points that is greater than 5000: ")

while int(number_of_points) <= 5000:
  number_of_points = input("\nInsert number of points greater than 5000: ")

number_of_points = int(number_of_points)

radius_of_circle = 1

number_of_cordinates_inside_circle = 0
number_of_cordinates_outside_circle = 0

while number_of_cordinates_inside_circle + number_of_cordinates_outside_circle <= number_of_points:
   x = random.uniform(0,radius_of_circle)
   y = random.uniform(0,radius_of_circle)
   distance_from_center = math.sqrt(x**2 + y**2)
   if distance_from_center <= radius_of_circle:
    number_of_cordinates_inside_circle += 1

   else:
    number_of_cordinates_outside_circle += 1

print("\nInside of quarter-circle:",number_of_cordinates_inside_circle)
print("Total number in square alone, outside of cirle:",number_of_cordinates_outside_circle)

print("\nPi is approximately:",(number_of_cordinates_inside_circle/number_of_points)* 4.0)


#code2
number_of_points = input("\nInsert a positive whole number of points that is greater than 5000: ")

while int(number_of_points) <= 5000:
  number_of_points = input("\nInsert number of points greater than 5000: ")

number_of_points = int(number_of_points)

radius_of_circle = 1

number_of_cordinates_inside_circle = 0
number_of_cordinates_outside_circle = 0

for i in range(0,number_of_points):
   x = random.uniform(0,radius_of_circle)
   y = random.uniform(0,radius_of_circle)
   distance_from_center = math.sqrt(x**2 + y**2)
   if distance_from_center <= radius_of_circle:
    number_of_cordinates_inside_circle += 1

   else:
    number_of_cordinates_outside_circle += 1

print("\nInside of quarter-circle:",number_of_cordinates_inside_circle)
print("Total number in square alone, outside of cirle:",number_of_cordinates_outside_circle)

print("\nPi is approximately:",(number_of_cordinates_inside_circle/number_of_points)* 4.0)
