#Ogochukwu Amaeze
#25/11/2022

my_book = open("book.txt", "r")
book_list = list(my_book)
#print(book_list.split())

count_words=0
travel=0
while travel<len(book_list):
  count_words+=len(book_list[travel].split())
  travel+=1
print("book.txt:\n\t\t",count_words)
  