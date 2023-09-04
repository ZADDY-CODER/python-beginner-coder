#Ogochukwu Amaeze
#25/11/2022
#this program create a book and adds numbers as strings of two to each line
#and prints the book

import random

def create_integer_file( filename, N):
    file_write = open(filename,'r+')
    for i in range(0,N):
        file_write.write(str(random.randint(0,1000)))
        file_write.write(' ')
        file_write.write(str(random.randint(0,1000)))
        file_write.write('\n')
    file_write.close()

create_integer_file("OGO.txt",10)

file_open=open("OGO.txt","r")
print("file:'OGO.txt' created:\n"+file_open.read())