with open ('phonetics.csv', 'r') as file:
    file_data = file.readlines()
    
file_dict = {n.split(',')[0]:n.split(',')[1].strip() for n in file_data}

name = input('what is your name: ')
name_list = list(name.upper())

phonetics = [file_dict[l] for l in name_list]
print(phonetics)

