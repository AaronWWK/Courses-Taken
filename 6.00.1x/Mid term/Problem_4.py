def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    result = 0
    result2 = num
    print(result2)
    exponent = 0
    for i in range(num):
        result = base**i - num
        if abs(result) < abs(result2):
            exponent = i

    return exponent
print(closest_power(4,16))
