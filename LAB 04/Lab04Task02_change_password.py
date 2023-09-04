#Ogochukwu Amaeze
#21/10/22

#code 1
password_old = str("secret")

print("***Change password***")
password_GUESS = input("Enter The Current Password: ")

while password_GUESS != password_old:
  password_GUESS = input("Incorrect: Current Password Needed:")

if password_GUESS == password_old:
  password_new = input("Enter The New Password: ")
  password_old = password_new # allowing the old password to become a new password
  print("Password successfully changed.")