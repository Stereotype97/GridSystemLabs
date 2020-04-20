H = 0.0001
K1 = 100
K2 = 100

l1 = 0.1
l2 = 0.1

x01 = l1
x02 = l2 + x01

def f1(x1, x2):
    return K2 * ((x2 - x1) - (x02 - x01)) - K1 * (x1 - x01)

def f2(x1, x2):
    return -K2 * ((x2 - x1) - (x02 - x01))

# Решение уравнений второго порядка
# Вводим вторую функцию y1 = y' = u

def Euler(xi, yi, ui, h = H):
    # Calculations of i + 1 element

    u_ = ui + h * f(xi, yi, ui)
    у_ = уi + h * ui # ui = f2(xi, y1,i, yi)
    # xi+1=xi+h

def Euler_local(x1i, x2i, yi, ui, f, h = H):
    # Calculations of i + 1 element

    u_ = ui + h * f(xi, yi, ui)
    у_ = уi + h * ui # ui = f2(xi, y1,i, yi)


def main():
    # Setting of started values
    t0 = 0
    x0 = 0

    # u = y' = dy/dx
    u01 = 0
    u02 = 0
    
    u1_list = []
    u1_list.append(u01) # first value
    u2_list = []
    u2_list.append(u02) # first value

    x1_list = []
    x1_list.append(x01 + 0.05) # 0.1 + 0.05
    x2_list = []
    x2_list.append(x02 + 0.05) # 0.1 + 0.1 + 0.05

    h = H
    i = 0
    t = t0
    t_end = 10
    while t < t_end:

        # Using calculated x1 value
        u1_new = u1_list[i] + h * f1(x1_list[i], x2_list[i]) # f = f(t,x,u)
        x1_new = x1_list[i] + h * u1_list[i] # ui = f2(xi, y1,i, yi)
        
        u1_list.append(u1_new)
        x1_list.append(x1_new)

        u2_new = u2_list[i] + h * f2(x1_new, x2_list[i])
        u2_list.append(u2_new)
        
        x2_new = x2_list[i] + h * u2_list[i]
        x2_list.append(x2_new)

        t += h

        i += 1

    count = i + 1
    for i in range(count):
        print("x1 = {x1} x2 = {x2} v1 = {v1} v2 = {v2}".format(x1=x1_list[i], x2=x2_list[i], v1=u1_list[i], v2=u2_list[i]))

if __name__ == "__main__":
    main()
