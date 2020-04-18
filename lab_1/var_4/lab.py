import math
import os

H = 0.01

def f(xi, yi, ui):
    # Example. Fill your function here
    return -yi

def func_to_check(x):
    return math.sin(x) + 2 * math.cos(x)

# Решение уравнений второго порядка
# Вводим вторую функцию y' = u
def euler_method_2(xi, yi, ui, func, h = H):
    # Calculations of i + 1 element

    u_ = ui + h * func(xi, yi, ui)
    y_ = yi + h * ui # ui = f2(xi, y1,i, yi)

    return y_, u_


def main():
    # Setting of started values
    x0 = 0
    y0 = 2

    # u = y' = dy/dx
    u0 = 1
    
    x_list = []
    x_list.append(x0) # first value

    y_list = []
    y_list.append(y0) # first value

    u_list = []
    u_list.append(u0) # first value

    h = H
    i = 0
    x = x0
    x_end = 10
    while x < x_end:
        # Choose your method of number calculations
        y_new, u_new = euler_method_2(x_list[i], y_list[i], u_list[i], f)
        u_list.append(u_new)
        y_list.append(y_new)

        x += h
        x_list.append(x)
        
        i += 1

    count = i + 1
    for i in range(count):
        print("i: {i:5}  x ={x:8.3f} y = {y:10.5f} checked = {checked:10.5f} u = {u:10.5f}".format(i=i, x=x_list[i], y=y_list[i],checked=func_to_check(x_list[i]), u=u_list[i]))


if __name__ == "__main__":
    main()
