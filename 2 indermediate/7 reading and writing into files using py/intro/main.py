# file = open("my_file.txt") # by default it opens in read mode
# content = file.read() #returns the content of the file as a string
# print(content)  
# file.close() # always close the file after using it to free up resources

#!======================================
# #using with statement to handle files. Automatically closes the file after the block is executed
# with open("my_file.txt") as file: # by default it opens in read mode
#     content = file.read() #returns the content of the file as a string
#     print(content)  

#!======================================
# #writing into a file
# with open("my_file.txt", mode='a') as file: 
#     file.write('i love eating chiken') #adds to existing content

#!======================================
#creating a non existing file
with open("new_file.txt", mode='w') as file:
    file.write('this is a new file') #creates a new file and writes into it
    
#!======================================
# #reading a file word by word
# with open("my_file.txt") as file1:
#     contents = file1.readlines() #returns a list of lines in the file
#     print(contents)
#     for line in contents:
#         words = line.split() #splits each line into words based on whitespace
#         for word in words:
#             print(word)
#!======================================
# #reading a file line by line
# with open("my_file.txt") as file2:
#     for line in file2:
#         print(line) #prints each line with an extra new line because each line already has a new line character at the end

#!======================================
# #deleting a file
# import os
# if os.path.exists("new_file.txt"): #check if the file exists
#     os.remove("new_file.txt")
    
# #deleting a folder
# if os.path.exists("new_folder"): #check if the folder exists
#     os.rmdir("new_folder") #folder must be empty to be deleted
    
#!======================================
# sending created file to a directory
import shutil
import os
if os.path.exists("new_file.txt"):
    shutil.move("new_file.txt", "2 indermediate/7 reading and writing into files using py/intro/finished/new_file.txt")