#📑📑COMPARISON OPERATORS
num_1 = 3
num_2 = 4
print(num_1 == num_2) #False
print(num_1 != num_2) #True
print(num_1 > num_2)  #False
print(num_1 < num_2)  #True
print(num_1 >= num_2) #False
print(num_1 <= num_2) #True

#📑📑AND returns true if all the variables evaluate to true
price = 1
print(price > 50 and price < 200) #returns true if price is between 50 and 200

#📑📑OR returns true if atleast one of the variables evaluate to true
print(price > 50 or price < 200) #true

#📑📑NOT returns the opposite of the variable
legal_age = True
print(f'Is of legal age: {not legal_age}')