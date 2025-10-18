# #!=========================================
import pandas
import csv

data = pandas.read_csv('squirrel_census.csv')
grey = []
red = []
black = []

colours = data["Primary Fur Color"]
for colour in colours:
    if colour == 'Gray':
        grey.append(colour)
    elif colour == 'Cinnamon':
        red.append(colour)
    elif colour == 'Black':
        black.append(colour)
        

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [len(grey), len(red), len(black)]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv('squirrel_count.csv')