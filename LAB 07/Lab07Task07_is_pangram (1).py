#Ogochukwu Amaeze
#19/11/2022
#This program will allow the user to input a sentence or word and check if it is a pangram

#sort words and sentences to alphabetical order
def SORT(word):
    return ''.join(sorted(word))
  
def pangrams(words):
  is_pangram = True
  alphabet=str("abcdefghijklmnopqrstuvwxyz")
  space=str(" abcdefghijklmnopqrstuvwxyz")#When sentences are placed into alphabetical order the space (" ") is placed in the index 0 postion. 
  #Therefore I need 1 lists containing all the alphabets and another list containing a space (" ") and all the alphabet
  if len(words)<25:
    is_pangram = False
  else:
      if (words == alphabet) or (words == space):
        is_pangram = True
      else:
        is_pangram = False
  return is_pangram

pangrams_CHECKING=input("Enter a list of words: ")
pangrams_CHECKING=SORT(set(pangrams_CHECKING.lower())) #Deletes all duplicate letters in list and changes all capital to lower case 
print("Is Pangram?",pangrams(pangrams_CHECKING))