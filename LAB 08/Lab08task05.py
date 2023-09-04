#Ogochukwu Amaeze
#30/11/2022

my_book = open("book.txt", "r")
book_list = list(my_book)

#function looks throug the book and returns the line containing the word desired
def filter_file(book, word, Word):
  count=0
  THE_LIST=[]
  COUNT=0
  while COUNT < len(book):
    line = book[COUNT].split()  
    while count<len(line):
      if line[count] == str(word) or line[count] == str(Word):
        THE_LIST.append(book[COUNT])
        break
      else:
        count+=1
    COUNT+=1   
    count=0
  return THE_LIST

#lister is the list of all the lines containing the word desired
lister=filter_file(book_list,"the","The")

#function creates a new book containing only the lines containing the word "The" from "book.txt"
def create_book(filename, N, words):
  file_write = open(filename,'x')
  for i in range(N):
    file_write.write(words[i])
    file_write.write("\n")
  file_write.close()

create_book("book_desired.txt",len(lister),lister)
print("""Searching file:  book.txt
   ...scanning lines for the search_word: 'the'
File: 
   book_desired.txt created containing lines with: 'the'""")