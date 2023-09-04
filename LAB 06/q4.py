#Ogochukwu Amaeze
#16/12/22
#this prgrame count the number of seperate vowels in a word or sentence

sentence=input("Enter a word or a sentence: ")
sentence=list(sentence.split())#turn str in to a list
sentence= "".join(sentence)#deleting space between words

#vowel chekers
vowel_a=0
vowel_e=0
vowel_i=0
vowel_o=0
vowel_u=0

#use for loop and if statement to find number of vowels
for i in sentence:
  if i == "a":
    vowel_a+=1
  elif i == "e":
    vowel_e+=1
  elif i == "i":
    vowel_i+=1
  elif i == "o":
    vowel_o+=1
  elif i == "u":
    vowel_u+=1

#print out results
print("\na\t"+str(vowel_a)+"\ne\t"+str(vowel_e)+"\ni\t"+str(vowel_i,)+"\no\t"+str(vowel_o)+"\nu\t"+str(vowel_u))