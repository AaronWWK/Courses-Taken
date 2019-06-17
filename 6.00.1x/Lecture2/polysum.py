import math
# def polysum(n,s):
#     area = (0.25*n*s*s)/math.tan(math.pi/n)
#     perimeter = n*s
#     sum = area + perimeter
#     return round(sum,4)

def polysum(n, s):

    area = (0.25*n*s*s)/(tan(pi/n))
    per = s*n
    suma = float(format(area + per**2, '.4f'))
    return suma


print(polysum(4,3))
