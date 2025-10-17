import os 

#get the base directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))

#full paths to the file
name_path = os.path.join(base_dir, '../mail merging/input/letters/names/invited_names.txt')
letter_path = os.path.join(base_dir, '../mail merging/input/letters/starting_letter.docx')
output_dir = os.path.join(base_dir, '../mail merging/output/readyToSend')

#getting names to be addressed to
with open(name_path) as names_file:
    names = names_file.readlines()

#creating the letters
with open(letter_path) as letter_file:
    letter_contents = letter_file.read()
    
for name in names:
    lines = name.strip() #remove spaces or \n
    personalized_letter = letter_contents.replace("[name]", lines)
    
    #create path to readyToSend folder
    file_path = os.path.join(output_dir, f"{lines}.txt")

    #saving the letters in readyToSend folder
    with open(file_path, mode='w') as file:
        file.write(personalized_letter)


        
