# x = 'pi'
# y = 't'
# x,y = y,x
# print(x,y)


# def f(x):
#     while x > 3:
#         f(x+1)
#
# f(x=3)
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
print(Square(-5))
