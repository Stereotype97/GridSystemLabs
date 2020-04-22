import os
import matplotlib.pyplot as plt
import random

def generate_color():
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    return color

def print_graphic(graphic_file_name, data_file_name):
    file_names = []
    file_names.append(data_file_name)
    print_graphics(graphic_file_name, file_names)

def print_graphics(graphic_file_name, data_file_names):
    plt.ioff()
    _, ax = plt.subplots()

    for data_file_name in data_file_names:
        x_list = []
        y_list = []
        
        with open(data_file_name, 'r') as data_file:
            lines = data_file.readlines()
            for line in lines:
                pair = line.split(',')
                x_list.append(float(pair[0]))
                y_list.append(float(pair[1]))
        data_file.close()
 
        ax.plot(x_list, y_list, 'k', linestyle='solid', color=generate_color())
 
    plt.savefig(graphic_file_name)
