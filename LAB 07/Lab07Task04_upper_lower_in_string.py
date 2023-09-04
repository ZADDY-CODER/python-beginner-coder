#Ogochukwu Amaeze
#18/11/22
#this program will identify the number of lower and upper casings in a given word also wlhe usig a list

words= str(input("Enter a word: "))

def casing(word):
  upper=0
  lower=0
  check=0
  
  while check<len(words):
    if words[check].isupper():
      upper+=1
      check+=1

    else:
      lower+=1
      check+=1

  return lower,upper
cases= casing(words)
print("There are",cases[1],"upper case letters in the word.\nThere are",cases[0],"lower case letters in the word.")
