#Ogochukwu Amaeze
#10/10/2022
#leapyear.py

LEAP = float(input("Enter a year to see if it is a leap-year:\n"))
if ( LEAP%100 != 0 or LEAP%400 == 0) and LEAP%4 == 0:
  print(True)

# first i allowed the the input (LEAP) to go into an OR gate, giving the conditions that if LEAP is not divisible by 100 or if LEAP is divisble by 400, then it is a Leap year.
# Then if LEAP met a high of low condition, this result would be passed through an AND gate of the condition that if LEAP is divisible by 4 then it is a leap year.
# Now if LEAP could not satisify either or of the 2 conditions of the OR gate a result of 0(low input) + 0(low input) giving in total 0(a low output).
# If LEAP could satisify atleast one of the 2 conditions of the OR gate then a result of 1(high input) + 0(low input) (regardless of order of which conditions were filled) giving in total 1(a high output)
# though if LEAP satisify both conditions of the OR gate then that would result in 1(a high output)
# Now this ouput of the OR gate would pass through the AND gate, under one more condition, and if LEAP could not satisfy the codition of the AND gate a result of (output of OR gate) x 0(input) giving the total of 0(a low output).
# both OR gate output and AND gate input had to be 1(a high output/input) to result in the "if" statement to be request to be printed(True)
# if either the OR gate output or the AND gate input were 0(low input?output) the "else statement" would be requested to be printed(False)

else:
  print(False)