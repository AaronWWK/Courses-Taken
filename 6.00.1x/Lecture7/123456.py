def abs(x):

    """Assumes x is an int Returns x if x>=0 and –x otherwise"""
    if x < -1:

        return -x
    else:

        return x

for i in range(-6,2):
    print('abs(',i,') is ',abs(i))
