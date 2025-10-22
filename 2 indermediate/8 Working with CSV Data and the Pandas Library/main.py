# # with open("weather_data.csv") as weater_data:
# #     data = weater_data.readlines()
# #     print(data)

# #!=========================================
# # import csv

# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file) #creates a reader object that can be iterated over to get each row of the csv file
# #     temperature = []
# #     for row in data:
# #         if row[1] != 'temp': #skipping the header row
# #             temperature.append(int(row[1]))
        
# #     print(temperature)
    
# #!=========================================
# import pandas

# data = pandas.read_csv('weather_data.csv') # dataframe=> 2 dimensional
# #print(data['temp']) # series => 1 dimensional

# data.dict = data.to_dict() # converting dataframe to dictionary
# #print(data.dict)

# temp_list = data['temp'].to_list() # converting series to list
# #sum(temp_list / len(temp_list))  # average using lists

# print(data['temp'].mean()) # average using pandas
# print(data['temp'].max()) # max temp

# print(data.condition) # accessing a column without using []
# print(data[data.day == 'Monday']) # accessing a row
# print(data[data.temp == data.temp.max()]) # accessing row with max temp

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# monday_temp_F = int(monday.temp) * 9/5 + 32
# print(monday_temp_F)

# #creating a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
# data_frame.to_csv('new_data.csv') # exporting dataframe to csv file

# #!=========================================
student_dict = {
    'student': ['angela', 'james', 'lily'],
    'score': [56, 76, 98]
}

import pandas

student_df = pandas.DataFrame(student_dict)

#*looping through a data frame
# for (key, value) in student_df.items():
#     print(key) #title(head) of each column
#     print(value) #data in each column

#*looping through rows of a data frame
for (index, row) in student_df.iterrows():
    print(row.student)
    
