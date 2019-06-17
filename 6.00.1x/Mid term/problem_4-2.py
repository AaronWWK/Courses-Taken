def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    #Write a function is_triangular that meets the specification below.
    #A triangular number is a number obtained by the continued summation of integers starting from 1.
    #For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
    """
    sum = 0
    i = 0
    while True:
        i = i + 1
        sum = sum + i
        if sum == k:
            return True
        elif sum > k:
            return False


print(is_triangular(10))
