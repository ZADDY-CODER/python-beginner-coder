import math	
#ogochukwu Amaeze
#07/10/2022
#square.py

PI = math.pi	
print('''Type an angle in degrees
      (i.e. 2.2, 44.013 etc.)''')
x = input("")
float_of_x = float(x)
angle_radians = float_of_x*PI / 180
sine_angle = math.sin(angle_radians)
sqrt_sine = (sine_angle)**(1/2)
print("The square-root of the sine of:" ,x, "degrees is\n" , sqrt_sine )