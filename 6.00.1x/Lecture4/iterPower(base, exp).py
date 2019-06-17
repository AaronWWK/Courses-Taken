def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * iterPower(base, exp - 1)



def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    if exp == 0:
        return result
    else:
        for i in range(0,exp):
            result *=base
    return result


print(iterPower(-5.0, 9))
