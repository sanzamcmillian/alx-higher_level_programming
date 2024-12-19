#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    divide = 0
    if my_list == []:
        return 0
    for element in my_list:
        result += element[0] * element[1]
        divide += element[1]
    result = result / divide
    return result
