def gcdIter(a,b):
    # if a > b :
    #     gcd = b
    # else:
    #     gcd = a
    gcd = min(a,b)  # use function


    while a%gcd != 0 or b % gcd != 0:
        gcd -= 1
    return gcd


def gcdRecur(a,b):
    gcd = min(a,b)
    if gcd == 0:
        return 0
    elif a%gcd == 0 and b%gcd == 0:
        return gcd
    else:
        return gcdRecur(gcd,max(a,b)%gcd)

# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
# 
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Your code here
#     divisor = 1
#     Big = max(a,b)
#     Small = min (a,b)
#
#     if min(a,b) == 0:
#         return Big
#     else:
#         divisor = gcdRecur(Small,Big%Small)
#     return divisor





print(gcdIter(10,45))

print(gcdRecur(124,8))
