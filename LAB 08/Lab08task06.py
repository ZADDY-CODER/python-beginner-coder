#Ogochukwu Amaeze

int_book = open("Integers_Example.txt", "r")
int_list = list(int_book.readlines())

#the function will create a list of all the str(numbers) as int(numbers)
def spliter(LIST):
  nums=[]
  index=0
  while index<len(LIST):
    num = list(LIST[index].split())
    for i in num:
      nums.append(int(i))
    index+=1
 
  return nums
  
all_nums = spliter(int_list)

#this function will create a book containing all the columns of the txt give as lists instead
def columns(filename, list):
  writer=open(filename, "w")
  colum_count=0
  while colum_count<len(list)//3:
    writer.write(str(list[colum_count]))
    writer.write(" ")
    writer.write(str(list[colum_count+100]))
    writer.write(" ")
    writer.write(str(list[colum_count+200]))
    writer.write("\n")
    colum_count+=1
  writer.close()

columns("transposing.txt", all_nums)

print("""Transposing file:  integers_example.txt
File:
     transpose.txt created.
         (See: columns converted to lines within.)""")