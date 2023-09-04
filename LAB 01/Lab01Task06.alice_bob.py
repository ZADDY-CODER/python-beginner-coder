#ogochukwu Amaeze
#07/10/22
#aliceandbob.py
y = str("Bob")
x = str("Alice")
print('''Type a name: if it's alice or bob
the program will print 'True' ''')
name = input()
#implied str.casefold to ingnore all variable of bob and alice as different strings
if name.casefold() == x.casefold() or name.casefold() == y.casefold():
  print(True)

else:
  print(False)