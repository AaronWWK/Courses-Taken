def polysum(n,s):
    import math

    sum = (n*s)**2 + 0.25*n*s*s/ math.tan((math.pi)/n)

    return round(sum,4)
