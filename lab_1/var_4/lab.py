import math
import os

H = 0.1

def func(xi, yi, ui):
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


# We have the Dif. equation, kind of y'' = f(x, y, y')
# 
# y' = u            (f - func)
# u' = f(x, y, y)   (g - func)
def runge_kutta_4_2(xi, yi, ui, func, h = H):
    # calculations of additional coeficients
    # all Ki are depending on f (only u(y') actually)
    # all Li are depending on g (our y'' function)

    # helper function, depending on u only
    def f(xi, yi, ui):
        return ui

    k1 = h * f(xi, yi, ui)
    l1 = h * func(xi, yi, ui)

    k2 = h * f(xi + h / 2, yi + k1 / 2, ui + l1 / 2)
    l2 = h * func(xi + h / 2, yi + k1 / 2, ui + l1 / 2)

    k3 = h * f(xi + h / 2, yi + k2 / 2, ui + l2 / 2)
    l3 = h * func(xi + h / 2, yi + k2 / 2, ui + l2 / 2)

    k4 = h * f(xi + h, yi + k3, ui + l3)
    l4 = h * func(xi + h, yi + k3, ui + l3)

    dy = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    du = (l1 + 2 * l2 + 2 * l3 + l4) / 6

    y_ = yi + dy
    u_ = ui + du

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
        y_new, u_new = runge_kutta_4_2(x_list[i], y_list[i], u_list[i], func)
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
