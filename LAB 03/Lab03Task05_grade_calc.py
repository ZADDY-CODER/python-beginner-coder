#Ogochukwu Amaeze
#14/10/2022


#code 1
per = float(input("Enter a percentage: 0.0 - 100.0%:"))
while per < 0 or per > 100:
  per = float(input("Try again: Enter between: 0.0-100.0 only:"))

if per >= 85 and per <= 100:
  print("Grade A")
elif per >= 70 and per <= 85:
  print("Grade B")
elif per >= 55 and per <= 70:
  print("Grade C")
elif per >= 40 and per <= 55:
  print("Grade D")
elif per >= 25 and per <= 40:
  print("Grade E")
else:
  print("Grade F")