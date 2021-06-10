import math
def input_x():
    x = int(input("faka kho-odineyithi ka x"))
    return x
def input_y():
    y = int(input("faka kho-odineyithi ka y"))
    return y
def input_name():
    name = input(" faka igama lepoyinti")
    return name
def calc_distance():
    distance = math.sqrt((0-input_x())*(0-input_x()) + (0-input_y())*(0-input_y()))
    return distance
def reflect_y():
    x = input_x() * (-1)
    return x
def reflect_x():
    y = input_y() * (-1)
    return y
def equation():
    gradient = int((0-input_y()) / (0-input_x()))
    print("y =", gradient, "x", "+", input_y())
def quadrant():
    if input_x() < 0 and input_y() > 0:
        print("NORTH WEST QUADRANT")
    if input_x() > 0 and input_y() > 0:
        print("NORTH EAST QUADRANT")
    if input_x() < 0 and input_y() < 0:
        print("SOUTH WEST QUADRANT")
    if input_x() > 0 and input_y() < 0:
        print("SOUTH EAST QUADRANT")

if __name__ == '__main__':
    xx = input_x()
    yy = input_y()
    nn = input_name()
    dd = calc_distance()
    rx = reflect_x()
    ry = reflect_y()
    equation()
    quadrant()




