
def num_to_Binary(num):
    if num < 0:
        isNeg = True
        num = abs(num)
    else:
        isNeg = False
    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num%2) + result
        num = num//2
    if isNeg:
        result = '-' + result
    return result

# num = -51
# print(num_to_Binary(num))

def Binary_to_num(Binary):
    num = 0
    str_ = str(Binary)
    Exp = len(str_) - 1
    for i in str_:
        if int(i) == 1:
            num += 2**Exp
        Exp -= 1
    return num
# Binary = 001101
# print(Binary_to_num(Binary))
