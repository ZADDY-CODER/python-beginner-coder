#Ogochukwu Amaeze
#07/10/22
#radians.py

import math

PI = math.pi

print("""an angle in degrees
      (i.e. 2.2, 44.013 etc.)\n""")
x = input("")
float_of_x = float(x)
print("Converting to" ,x, "radians...")
print("The angle in radians is:", float_of_x * PI / 180)