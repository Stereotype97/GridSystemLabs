import math
import os
import sys

sys.path.append('../')

from graphic_for_lab import print_graphic

H = 0.1

def func(xi, yi, ui):
    # Example. Fill your function here
    return -yi

# def func_to_check(x):
#     return math.sin(x) + 2 * math.cos(x)

# Решение уравнений второго порядка
# Вводим вторую функцию y' = u
def euler_method_2(xi, yi, ui, func, h = H):
    # Calculations of i + 1 element

    u_ = ui + h * func(xi, yi, ui)
    y_ = yi + h * ui # ui = f2(xi, y1,i, yi)

    return y_, u_

# def euler_method_improved_2(xi, yi, ui, func, is_first_iteration, h = H):
#     step = h if not is_first_iteration else h / 2
#     u_ = ui + step  * func(xi, yi, ui)
#     y_ = yi + h * u_

#     return y_, u_

def main():
    # Setting of started values
    x0 = 0
    y0 = 2

    # u = y' = dy/dx
    u0 = 1
    
    x_list = [] # Time 
    x_list.append(x0) # first value

    y_list = [] # Position
    y_list.append(y0) # first value

    u_list = [] # Velocity
    u_list.append(u0) # first value

    h = H
    i = 0
    x = x0
    x_end = 10

    while x < x_end:
        # Choose your method of number calculations
        y_new, u_new = euler_method_2(x_list[i], y_list[i], u_list[i], func)
        
        u_list.append(u_new)
        y_list.append(y_new)

        x += h
        x_list.append(x)
        
        i += 1

    count = i + 1

    data_file_name = 'data_of_body_displacement_versus_time.txt'
    f = open(data_file_name, 'w')

    for i in range(count):
        f.write(str(x_list[i]) + ',' + str(y_list[i]) + '\n')
    f.close()

    print_graphic('plot_of_body_displacement_versus_time.png', data_file_name)

    data_file_name = 'data_of_velocity_versus_time.txt'
    f = open(data_file_name, 'w')

    for i in range(count):
        f.write(str(x_list[i]) + ',' + str(u_list[i]) + '\n')
    f.close()

    print_graphic('plot_of_velocity_versus_time.png', data_file_name)

if __name__ == "__main__":
    main()
