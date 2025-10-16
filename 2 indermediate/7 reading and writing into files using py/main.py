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
#writing into a file
with open("my_file.txt", mode='a') as file: 
    file.write('i love eating chiken') #adds to existing content

#!======================================
#creating a non existing file
with open("new_file.txt", mode='w') as file:
    file.write('this is a new file') #creates a new file and writes into it